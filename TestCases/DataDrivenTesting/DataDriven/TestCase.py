import json
import jsonpath
import requests
import openpyxl
from DataDriver import Library


def test_add_multiple_students():
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails'
    file = open(
        "E:\PersonalHyd\Python\Programs\SeleniumInPython\TestCases\StudentDetails\TestCases\student_data.json", "r")
    json_request = json.loads(file.read())

    obj = Library.Common(
        "E:\\PersonalHyd\\Python\\Programs\\SeleniumInPython\\TestCases\\DataDrivenTesting\\testData.xlsx", "Sheet1")
    col = obj.fetch_col_count()
    keyList = obj.fetch_key_names()
    rows = obj.fetch_row_count()

    for i in range(2, rows+1):
        updated_json_request = obj.update_request_with_data(
            i, json_request, keyList)
        response = requests.post(API_URL, updated_json_request)
        print(response.text)
