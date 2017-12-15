# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import requests
from bs4 import BeautifulSoup
import json

def get_one_page(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    response = requests.get(url,headers=headers)

    if response.status_code==200:
        return response.text
    return None

def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    items = soup.find_all('dd')
    info=[]
    for item in items:        
#        yield {
#            'movie_name' :item.find('p',class_='name').a['title'],
#            'star':item.find('p',class_='star').text.strip()[3:],
#            'release_time':item.find('p',class_='releasetime').text[5:],
#            'store':item.find('p',class_='score').find('i',class_='integer').text+'.'+item.find('p',class_='score').find('i',class_='fraction').text          
#                }
        item_info=[]
        movie_name=item.find('p',class_='name').a['title']        
        star=item.find('p',class_='star').text.strip()[3:]
        release_time=item.find('p',class_='releasetime').text[5:]
        score=item.find('p',class_='score').find('i',class_='integer').text+'.'+item.find('p',class_='score').find('i',class_='fraction').text      
        item_info.append('movie_name:'+movie_name)
        item_info.append('star:'+star)
        item_info.append('release_time:'+release_time)
        item_info.append('score:'+score)
        info.append(item_info)
    return info
        
        


def write_into_file(content):
    with open('/home/python/maoyanmovie/result.txt','a') as f:
        f.write((str(content)) + '\n')
        f.close()

def main():
    url = "http://maoyan.com/board/4?offset=0"
    html = get_one_page(url)
    movies = parse_one_page(html)
#    write_into_file(movies)
    print(movies)

 
    
    
if __name__=="__main__":
    main()
    

