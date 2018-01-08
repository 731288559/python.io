import requests
import bs4
import time
import pymysql
from selenium import webdriver
import plotly
plotly.tools.set_credentials_file(username='731288559', api_key='Y7CeXd3cAadHNuFuGYIb')

import plotly.plotly as py
from plotly.graph_objs import *

con = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    db="python",
    port=3306,
    use_unicode=True,
    charset="utf8"
)
cur = con.cursor()

sql = '''select play_num_raw, count(*) as num
        from data
        group by play_num_raw'''

cur.execute(sql)
result = cur.fetchall()
# print(result)
id=[]
play_r =[]
for field in result:
        id.append(field[0])
        play_r.append(int(field[1]))
play_n = Scatter(
            x=id,
            y=play_r,
            name='play_num distribution'
        )
data = Data([play_n])

py.plot(data, filename = 'play_num distribution')

sql = '''select v_hour, count(*) as num
from data
group by v_hour'''

cur.execute(sql)
result = cur.fetchall()
# print(result)
xx =[]
yy =[]
for field in result:
        xx.append(field[0])
        yy.append(int(field[1]))
play_n = Scatter(
            x=xx,
            y=yy,
            name='time distribution'
        )
data = Data([play_n])

py.plot(data, filename = 'time distribution')

sql = '''
select v_date, count(*) as num
from data 
group by v_date
order by v_date
'''

cur.execute(sql)
result = cur.fetchall()
# print(result)
xx =[]
yy =[]
for field in result:
        xx.append(field[0])
        yy.append(int(field[1]))
play_n = Scatter(
            x=xx,
            y=yy,
            name='date distribution'
        )
data = Data([play_n])

py.plot(data, filename = 'date distribution')