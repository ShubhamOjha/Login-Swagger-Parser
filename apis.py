import requests
import json
import xlwt 
from xlwt import Workbook

URL = 'http://127.0.0.1:8000/docs/api-docs/'
LOGIN_URL = 'http://127.0.0.1:8000/login_swagger/'
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

session = requests.session()

session.get(LOGIN_URL)
csrftoken = session.cookies['csrftoken']

login_data = {'username': USERNAME,
              'password': PASSWORD,
              'csrfmiddlewaretoken': csrftoken}
session.post(LOGIN_URL, data=login_data)

req = session.get(URL)
json_data = json.loads(req.text)


wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1') 

  

row = 0
for i in range(len(json_data['apis'])):
	req1 = session.get(URL+json_data['apis'][i]['path'])
	json_data1 = json.loads(req1.text)
	for j in range(len(json_data1['apis'])):
		for k in range(len(json_data1['apis'][j]['operations'])):
			sheet1.write(row,0,json_data1['apis'][j]['operations'][k]['method'])
			sheet1.write(row,1,json_data1['apis'][j]['path'])
			row += 1
		
wb.save('LOGIN_SWAGGER.xls') 

