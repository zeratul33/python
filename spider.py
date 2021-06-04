import xlwt
import urllib.request
import requests
import time
import json
import re
import pandas as pd
from pandas import DataFrame

from xlwt.Formatting import Font

url = "http://74.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406112931804091546_1622624859371&pn=1&pz=4500&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1622624859547"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
response = urllib.request.urlopen(url)

comments = requests.get(url,headers = header).text

def data_result(comments):                           #json字符串处理

    data_result = re.sub('jQuery(.*?)\(',' ',comments)
    data_result2 = re.sub('\)\;',' ',data_result)
    json_sub = json.loads(data_result2)
    return json_sub

def create_sheet():                             #创建EXCEL
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('result')
    font = xlwt.Font()
    sheet.write(0,0,'代码')
    sheet.write(0,1,'名称')
    sheet.write(0,2,'最新价')
    sheet.write(0,3,'涨跌幅')
    sheet.write(0,4,'涨跌额')
    sheet.write(0,5,'成交量（手）')
    sheet.write(0,6,'成交额')
    sheet.write(0,7,'振幅')
    sheet.write(0,8,'换手率')
    sheet.write(0,9,'市盈率')
    sheet.write(0,10,'最高')
    sheet.write(0,11,'最低')
    sheet.write(0,12,'今开')
    sheet.write(0,13,'昨收')
    sheet.write(0,14,'市净率')
    workbook.save('result.xls')
    
def save_sheet(i,data_result):
    data = pd.read_excel('result.xls',sheet_name='result')
    data.loc[i] = [ data_result['data']['diff'][i-1]['f12'],
                data_result['data']['diff'][i-1]['f14'],
                data_result['data']['diff'][i-1]['f2'],
                data_result['data']['diff'][i-1]['f3'],
                data_result['data']['diff'][i-1]['f4'],
                data_result['data']['diff'][i-1]['f5'],
                data_result['data']['diff'][i-1]['f6'],
                data_result['data']['diff'][i-1]['f7'],
                data_result['data']['diff'][i-1]['f8'],
                data_result['data']['diff'][i-1]['f9'],
                data_result['data']['diff'][i-1]['f15'],
                data_result['data']['diff'][i-1]['f16'],
                data_result['data']['diff'][i-1]['f17'],
                data_result['data']['diff'][i-1]['f18'],
                data_result['data']['diff'][i-1]['f23']

    ]
    #print(data_result)
    DataFrame(data).to_excel('result.xls',sheet_name='result',index=False,header=-1)






total = data_result(comments)['data']['total']
create_sheet()
#print(type(data_result(comments)['data']['diff'][0]['f12']))
data_result = data_result(comments)
for i in range(0,total):
     save_sheet(i+1,data_result)
     print("已写入第%d列数据"%i)
# for j in range (0,20):
#     print(data_result['data']['diff'][j]['f12'],
#         data_result['data']['diff'][j]['f14'],
#         data_result['data']['diff'][j]['f2'],
#         data_result['data']['diff'][j]['f3'],
#         data_result['data']['diff'][j]['f4'],
#         data_result['data']['diff'][j]['f5'],
#         data_result['data']['diff'][j]['f6'],
#         data_result['data']['diff'][j]['f7'],
#         data_result['data']['diff'][j]['f8'],
#         data_result['data']['diff'][j]['f9'],
#         data_result['data']['diff'][j]['f15'],
#         data_result['data']['diff'][j]['f16'],
#         data_result['data']['diff'][j]['f17'],
#         data_result['data']['diff'][j]['f18'],
#         data_result['data']['diff'][j]['f23'])
print("complete")

