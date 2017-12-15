# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import requests
from bs4 import BeautifulSoup

def get_one_page(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    response = requests.get(url,headers=headers)

    if response.status_code==200:
        return response.text
    return None

def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    item = soup.find_all('dd')
    return item


#def main():
#    url = "http://maoyan.com/board/4?offset=0"
#    html = get_one_page(url)
#    movies = parse_one_page(html)
#    print(movies)
#    print(html)    
    
    
if __name__=="__main__":
    url = "http://maoyan.com/board/4?offset=0"
    html = get_one_page(url)
    movies = parse_one_page(html)
    print(movies)
    

