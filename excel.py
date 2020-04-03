#import required modules

import http.client
import mimetypes
import json
import openpyxl
from openpyxl.utils import get_column_letter

#make a request
conn = http.client.HTTPSConnection("thevirustracker.com")
payload = ''
headers = {}
conn.request("GET", "/timeline/map-data.json", payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
js = json.loads(data) #receive json and load

#open excel sheet to edit
wb_output = openpyxl.load_workbook('excel_output.xlsx')
sheet_output = wb_output['Sheet1']

#edit titles of excel sheet
sheet_output['A1'] = 'Date'
sheet_output['B1'] = 'Country Code'
sheet_output['C1'] = 'Cases'
sheet_output['D1'] = 'Deaths'
sheet_output['E1'] = 'Recovered'

i = 0

while True:

    if js['data'][i]['countrycode'] == "":
            break

    #add data to excel sheet
    sheet_output['A' + str(i + 2)] = js['data'][i]['date']
    sheet_output['B' + str(i + 2)] = js['data'][i]['countrycode']
    sheet_output['C' + str(i + 2)] = js['data'][i]['cases']
    sheet_output['D' + str(i + 2)] = js['data'][i]['deaths']
    sheet_output['E' + str(i + 2)] = js['data'][i]['recovered']

    i += 1

#save the excel sheet
wb_output.save('excel_output.xlsx')
print('Output written to file!')
