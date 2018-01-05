import requests
import bs4
import re
import time
import pymysql
from selenium import webdriver

con = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    db="python",
    port=3306,
    use_unicode=True,
    charset="utf8"
)
cursor = con.cursor()

driver = webdriver.Chrome()
count = 0
for i in range(1, 1296 , 1):
    url = 'https://www.bilibili.com/v/life/funny/?spm_id_from=333.10.life_funny.3#/all/click/0/{}/2017-11-01,2018-01-01'.format(
        str(i))
    driver.get(url)
    # print(i)
    if i == 1:
        elements = driver.find_elements_by_class_name('mod-1')
        for element in elements:
            element.click()

    time.sleep(2)
    html = driver.page_source#获取网页的html数据
    soup = bs4.BeautifulSoup(html,'lxml')#对html进行解析
    r = soup.find_all('div',class_='r')
    for tag in r:
        title = str(tag.find('a',class_='title').text)
        href = str(tag.find('a',class_='title').get('href'))
        spans = tag.find_all('span',class_='v-info-i')
        play_num = str(spans[0].find('span').text)
        dm_num = str(spans[1].find('span').text)
        collect_num = str(spans[2].find('span').text)
        up_info = tag.find('div',class_='up-info')
        v_author = str(up_info.find('a',class_='v-author').text)
        v_date = str(up_info.find('span').text)
        count = count + 1
        print(title,href,play_num,dm_num,collect_num,v_author,v_date)
        sql = "insert into bilibili_funny_all(title,href,play_num,dm_num,collect_num,v_author,v_date) values('" \
              + title + "','" +href + "','" + play_num + "','" + dm_num + "','" + collect_num + "','" \
              + v_author + "','" + v_date +"')"
        # print(sql)
        cursor.execute(sql)
        con.commit()
print(count)
# av_num,title,play_num,dm_num,v_author,v_date,collect_num
# error in 961:彩虹(●'◡'●)ﾉ♥猪 , 1057
# 1023-900 miss (400-415)
