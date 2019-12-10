#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 00:35:19 2019

@author: crzy
"""
import re

# Array de termos chaves

# O quanto aqueles termos poderiam ser perpassados desde diferentes graus de complexidade

# Fazer comunicar com a ontologia Mental_Health.has_theme .has_instance

def get_matches(obj):
    
    keywords_arr = []
    keywords_arr.extend(["saude mental", "setembro amararelo", "felicidade", 
                         "feliz", "depressao", "bem estar", "suicidio"])
    
    for keyword in keywords_arr:
        regx = re.compile(f'.*saude mental.*', obj)
        print(regx)
        
