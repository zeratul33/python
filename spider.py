import bs4
import urllib.request
import requests
import time
import json
import re

url = "http://74.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406112931804091546_1622624859371&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1622624859547"
response = urllib.request.urlopen(url)
#print(response)
comments = requests.get(url)
pat = '"diff":\[\{.*?\}\]'
#comments = comments.encoding('utf-8')
#print(comments.text)
data = re.compile(pat,re.S).findall(comments.text)
data = json.loads(data)
print(data)

