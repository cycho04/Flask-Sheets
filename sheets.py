from googleapiclient import discovery
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# user input
first = str(input('First Name: '))
last = str(input('Last Name: '))
name = "%s, %s" % (last, first)
casino = str(input('Casino: '))
title = str(input('Title: '))
hired = str(input('Hired Date: '))
EIN = int(input('EIN: '))


# what we want access to, need to specifiy api
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']


# create credential and authorize
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)
authorize = gspread.authorize(credentials)
# Python client library for Google APIs
service = discovery.build('sheets', 'v4', credentials=credentials)

# select workbooks
database_worksheet = authorize.open('Test-Database')
info_list_worksheet = authorize.open('Test-InfoList')
attendance_worksheet = authorize.open('Test-Attendance')


# Database
# select original spreadsheet
original_db = database_worksheet.worksheet('OGPY')
# duplicate
original_db.duplicate(new_sheet_name=name)
# select new worksheet
new_db = database_worksheet.worksheet(name)
# updates name in Database
new_db.update_acell('A3', value=name)


# Attendance
original_attendance = attendance_worksheet.worksheet('OGPY')
original_attendance.duplicate(new_sheet_name=name)
new_attendance = attendance_worksheet.worksheet(name)
new_attendance.update_acell('F1', value=name)


# Info List
row = [name, '', '', '', '', '', casino, '', title,
       hired, '', '', EIN, '', '', '', '', name]
original_infolist = info_list_worksheet.worksheet('Employee List')
# append to bottom
original_infolist.append_row(row)


# Adding protections
# sheet ids
database_id = '1KzElJIZSS7MHgPcYsb01xl5Ea2L1pnPwBlHqRQ5TDus'
attendance_id = '1ANUPd9DzUFSGth_rjAK-xTkuD7f0CczMMgiP-X5n-Zs'


def batch_update_spreadsheet_request_body(id):
    return {
        "requests": [
            {
                "addProtectedRange": {
                    "protectedRange": {

                        "range": {
                            "sheetId": id
                        },
                        "unprotectedRanges": [
                            {
                                "sheetId": id,
                                "startColumnIndex": 0,
                                "endColumnIndex": 2,
                                "startRowIndex": 2,
                                "endRowIndex": 3
                            }
                        ]
                    }
                }
            }
        ]
    }


db_request = service.spreadsheets().batchUpdate(spreadsheetId=database_id,
                                                body=batch_update_spreadsheet_request_body(new_db.id))
db_response = db_request.execute()

attendance_request = service.spreadsheets().batchUpdate(spreadsheetId=attendance_id,
                                                        body=batch_update_spreadsheet_request_body(new_attendance.id))
attendance_response = attendance_request.execute()
