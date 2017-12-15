#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 20:53:38 2017

@author: python
"""

import requests
from bs4 import BeautifulSoup

url = "http://maoyan.com/board/4?offset=0"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text,'lxml')

movies = soup.find_all('dd')

for item in movies:
    print(item.find('p',class_='name'))