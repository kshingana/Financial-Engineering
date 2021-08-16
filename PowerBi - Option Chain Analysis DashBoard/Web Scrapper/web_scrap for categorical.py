# import js as js
# import numpy as np
# import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
import mysql.connector
# from nsetools import Nse
import datetime
import time

mydb = mysql.connector.connect(host="localhost", user='root', passwd='root', database='stock')
mycursor = mydb.cursor()

st_list = []
url = 'https://www.oipulse.com/app/connecting-dots'

agent = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
page = requests.get(url, headers=agent)
soup = BS(page.content, 'lxml')
#data = soup.find_all('tr', {"class": "common-table-item u-clickable"})
#final_data = []
print(soup)