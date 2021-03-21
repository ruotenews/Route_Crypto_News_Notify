#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author : GordonWei
#Date : Aug/06/19
#comment : Scrapying ITHome Today's News 

import requests, re, time, lineTool
from bs4 import BeautifulSoup

today = time.strftime('%Y-%m-%d')
lineToken = 'gtb1g34iKkSExaCnz2ZpCdZDYu5X7SgRuQZlckEXV6I'
ithome_site = 'https://siamblockchain.com/category/news/feed/'
indexRes = requests.get(ithome_site)
indexSoup = BeautifulSoup(indexRes.text, 'html.parser')
pages = indexSoup.find_all('span', class_ = 'views-field')

for n in pages:
        if n.find('p', text = re.compile(today)):
                if n.find('div'):
                        title = n.find('p', class_ = 'title').text
                        href = n.find('a')['href']
                botText = (today, title, 'https://siamblockchain.com/' + href)
                lineTool.lineNotify(lineToken, botText)
