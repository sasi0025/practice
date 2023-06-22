import imaplib
import inspect
import logging
import re

import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class Base:


    driver = webdriver.Chrome()

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_otp(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')

        email_username = 'sasikumar@neokred.tech'
        email_password = '9047317209@sasi'

        mail.login(email_username, email_password)
        mail.select('INBOX')

        _, message_ids = mail.search(None, 'SUBJECT "OTP Verification for Admin Login"')

        otp = None

        if message_ids and len(message_ids[0].split()) > 0:
            latest_message_id = message_ids[0].split()[-1]
            _, message_data = mail.fetch(latest_message_id, '(RFC822)')

            for response_part in message_data:
                if isinstance(response_part, tuple):
                    message_content = response_part[1].decode('utf-8')

                    otp_pattern = r'\b\d{6}\b'
                    match = re.search(otp_pattern, message_content)

                    if match:
                        otp = match.group()

        mail.logout()

        return otp

