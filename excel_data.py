import openpyxl

class TestData:
    @staticmethod
    def getTestData():
        workbook = openpyxl.load_workbook("C:\\Users\\sasikumar\\Documents\\50data.xlsx")
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            test_case = {
                'username': row[1],
                'password': row[2],
                'otp': row[3]
            }
            data.append(test_case)
        return data


