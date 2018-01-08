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
layout = Layout(title="time distribution")
fig = Figure(data=data, layout=layout)
py.plot(fig, filename = 'time distribution')

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
layout = Layout(title="date distribution")
fig = Figure(data=data, layout=layout)
py.plot(fig, filename = 'date distribution')

condition = ["BETWEEN '0' and '1000' ","BETWEEN '1000' and '100000' ","> 100000"]
i=0
yy=[]
for i in range(3):
    sql = '''
    select sum(v_num)
    from
    (
    select play_num_raw,count(*) as v_num
    from data
    where play_num_raw '''+condition[i]+'''
    group by play_num_raw
    )as a
    '''
    cur.execute(sql)
    result = cur.fetchall()
    # print(result)
    for field in result:
        yy.append(int(field[0]))
dataset = {'labels': condition,
           'values': yy}
data_g = []
tr_p = Pie(
    labels=dataset['labels'],
    values=dataset['values']
)
data_g.append(tr_p)
layout = Layout(title="play_n distribution")
fig = Figure(data=data_g, layout=layout)
py.plot(fig, filename="play_n distribution")


sql = '''
SELECT v_author,count(*) as work_num,avg(play_num_raw) as avg_p,
			avg(dm_num_raw) as avg_d,avg(collect_num_raw) as avg_c
FROM `data`
group by v_author
having avg_p>=200000 and work_num>=3 and avg_d>1000 and avg_c>1000
order by avg_p desc
'''

cur.execute(sql)
result = cur.fetchall()
# print(result)
xx =[]
yy =[]
for field in result:
        xx.append(field[0])
        yy.append(int(field[2]))
play_n = Scatter(
            x=xx,
            y=yy,
            name='excellent v_author'
        )
data = Data([play_n])
layout = Layout(title="excellent v_author")
fig = Figure(data=data, layout=layout)
py.plot(fig, filename = 'excellent v_author')