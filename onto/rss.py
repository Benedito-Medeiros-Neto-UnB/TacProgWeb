#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:06:24 2019

@author: crzy
"""

import feedparser
import re
#from elementpath import xml

class RssParser():
    feedurl = ""

    def __init__(self, paramrssurl):
        print(paramrssurl)
        self.feedurl = paramrssurl
        self.parse()

    # Define termos de busca no RSS Feed
    def get_matches(self, regex_term, str):
        regx = re.search('.*{}.*'.format(regex_term[1:]), str)
        if (regx != None): 
            print(str)
            return True
    
    def is_last_page(self):
        feedparsed = feedparser.parse(self.feedurl)
        if (len(feedparsed.entries) == 0):
            return False
        else:
            return True
        
    def parse(self):
        feedparsed = feedparser.parse(self.feedurl)
        print("Getting Feed Data")
        for post in feedparsed.entries:
            #print("\n-------------\n")
            
            search = post.title
            #print(search)
            if(self.get_matches("felicidade", search)):
                print(post.link)
                print(post.author)
                print(post.published)
                print(post.href)

            #print(post.title)
            #print(post.link) # 
            #print(post.author)
            #print(post.published)
            #print(post.description)
            #print(post)
            #print(xml.etree.ElementTree.fromstring(post.description).itertext())

# Main    

page_index = 1
cons = True

while(cons):
    
    url = "https://theintercept.com/feed/?lang=pt&paged=" + str(page_index)
    parser = RssParser(url)
    cons = parser.is_last_page()
    page_index += 1

# https://outraspalavras.net/feed/?paged=
# https://diplomatique.org.br/feed/?paged=
    
# Funcao para atualizar a ontologia/Feed

parser = RssParser


