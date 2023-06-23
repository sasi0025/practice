import os
import pytest
from selenium import webdriver
import time
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver")

    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))

            log_file = report.nodeid.replace("::", "_") + ".log"
            _capture_logs(log_file)
            if os.path.isfile(log_file):
                with open(log_file, 'r') as f:
                    log_content = f.read()
                    log_html = f'<pre>{log_content}</pre>'
                    extra.append(pytest_html.extras.html(log_html))

        report.extra = extra

        if not report.skipped:
            request = item._request
            email_report(request)

def _capture_screenshot(name):
    global driver
    driver.get_screenshot_as_file(name)

def _capture_logs(log_file):
    logger = logging.getLogger()
    handlers = logger.handlers
    if handlers:
        file_handler = handlers[0]
        if isinstance(file_handler, logging.FileHandler):
            log_file_path = file_handler.baseFilename
            with open(log_file_path, 'r') as src, open(log_file, 'w') as dest:
                dest.write(src.read())

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_FROM = 'sasikumar@neokred.tech'
EMAIL_PASSWORD = '9047317209@sasi'
EMAIL_TO = 'sasij4565@gmail.com'

@pytest.fixture(scope="class")
def email_sender():
    sender = EmailSender()
    yield sender
    sender.close()

class EmailSender:
    def __init__(self):
        self.msg = MIMEMultipart()
        self.msg['From'] = EMAIL_FROM
        self.msg['To'] = EMAIL_TO
        self.server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        self.server.starttls()
        self.server.login(EMAIL_FROM, EMAIL_PASSWORD)

    def send_email(self, test_name, test_result):
        self.msg['Subject'] = f"Test {test_name} {test_result}"
        body = f"Test {test_name} {test_result}"
        self.msg.attach(MIMEText(body, 'plain'))
        self.server.send_message(self.msg)

    def close(self):
        self.server.quit()

    def _capture_screenshot(self, name):
        self.driver.get_screenshot_as_file(name)

def generate_html_report(test_name):
    # Generate visualization graph
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4, 5], [1, 4, 2, 3, 5])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Sample Graph')
    plt.savefig('graph.png')

    # Create the HTML report
    report_html = f'''
    <html>
    <head></head>
    <body>
        <h2>Test Result: {test_name}</h2>
        <h3>Visualization Graph:</h3>
        <img src="graph.png" alt="graph" style="width: 400px;height: 300px;"><br>
        <h3>Logs:</h3>
        <pre>{get_logs()}</pre><br>
        <h3>Screenshot:</h3>
        <img src="{get_screenshot_filename()}" alt="screenshot" style="width: 400px;height: 300px;">
    </body>
    </html>
    '''

    # Send the email with the HTML report
    email_sender.send_email(test_name, report_html)

def get_logs():
    logger = logging.getLogger()
    log_content = ''
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            with open(handler.baseFilename, 'r') as log_file:
                log_content += log_file.read() + '\n'
    return log_content

def get_screenshot_filename():
    timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    return f'screenshot_{timestamp}.png'

email_sender._capture_screenshot = _capture_screenshot
