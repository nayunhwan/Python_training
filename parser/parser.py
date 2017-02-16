#-*- coding: utf-8 -*-

from urllib import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time

data = [];
for PageNum in range(1, 10):
    webpage = urlopen('http://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI&page' + str(PageNum))
    html = BeautifulSoup(webpage, "lxml")
    li = html.find_all("tr")

    for i in range(2, len(li)):
        if ((i >= 2 and i <= 4)) or (i >= 9 and i <= 11):
            itemList = li[i].find_all("td")

            data.append([itemList[0].get_text(),itemList[1].get_text(), itemList[4].get_text()]);
            print(data)

result_file = pd.DataFrame(data)
result_file = result_file.transpose()
result_file.column = {'DATE', 'POINT', 'TRADE_VOL'}
result_file.to_csv("C:/Users/noonoo/PycharmProjects/untitled/Homework/웹 크롤러 연습.csv", sep=',', header=True, index=False, index_label=False)