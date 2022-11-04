import xlrd
from Library.config import Config
from selenium import webdriver


class ReadExcel:
    """Includes methods for reading locators and data from excel sheet"""

    def read_testdata(self, sheetname):

        wb = xlrd.open_workbook(Config.TESTDATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()  # generator object
        header = next(rows)
        data = []
        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)

        return data

    def read_locators(self, sheetname):

        wb = xlrd.open_workbook(Config.LOCATER_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)

        dict_ = {}
        for row in rows:
            dict_[row[0].value] = (row[1].value, row[2].value)

        return dict_
