import time
import datetime
import requests
import json
import mysql.connector
import pandas as pd
import sqlite3

mydb = mysql.connector.connect(host="localhost",user='root',passwd = 'root', database = 'newOI')
mycursor = mydb.cursor()
nse_url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
symbols = ['BANKNIFTY', 'NIFTY']
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',


        'accept-language': 'en,gu;q=0.9,hi;q=0.8',
        'accept-encoding': 'gzip, deflate, br'
    }


expiry_dt = '22-Jul-2021'
'''while True:
    page = requests.get(nse_url, headers=headers)
    k = json.loads(page.text)
    #print(k)
    exp_dt = '22-jul-2021'
    lower_range = 12500
    upper_range = 15500
    CE = []
    PE = []
    l = (k['records']['data'])
    #print(l)
'''

page = requests.get(nse_url, headers=headers)
dajs = json.loads(page.text)
print(dajs)