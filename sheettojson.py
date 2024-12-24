from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

def loadsheet():
    #시트 선택하기
    #시트를 리스트로 복사하기
    global sheetcopy
    sheetcopy = []
    sheetcopy = sheet.get_all_values()

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

#키 값 경로 
json_key_path = "key.json"

credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
gc = gspread.authorize(credential)

#스프레드시트 url 가져오기
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1HSYx4lOOKBX2GyDgWQs1otd9tIoZeBtovH50kA05LII"

doc = gc.open_by_url(spreadsheet_url)

sheet = doc.worksheet("봇용")

loadsheet()

final = "dict = " + str(sheetcopy)

with open("dict.json", 'w', encoding='UTF-8') as outfile:
    json.dump(final, outfile, indent=4, ensure_ascii=False)