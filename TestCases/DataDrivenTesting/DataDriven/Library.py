import json
import jsonpath
import requests
import openpyxl


class Common():
    def __init__(self, FileNamePath, SheetName):
        global wk
        global sh
        wk = openpyxl.load_workbook(FileNamePath)
        sh = wk[SheetName]

    def fetch_row_count(self):
        rows = sh.max_row
        return rows

    def fetch_col_count(self):
        col = sh.max_column
        return col

    def fetch_key_names(self):
        c = sh.max_column
        li = []
        for i in range(1, c+1):
            cell = sh.cell(row=1, column=i)
            li.insert(i-1, cell.value)
        return li

    def update_request_with_data(self, rowNum, jsonRequest, keylist):
        c = sh.max_column
        for i in range(1, c+1):
            cell = sh.cell(row=rowNum, column=i)
            jsonRequest[keylist[i-1]] = cell.value

        return jsonRequest
