#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 02:04:32 2019

@author: crzy
"""

from owlready2 import *
import re
onto_path.append(".")
onto = get_ontology("http://127.0.0.1/root_ontology.owl").load()
onto3 = get_ontology("https://127.0.0.1/onto_model_article.owl").load()
onto2 = get_ontology("https://127.0.0.1/onto_aux_finale.owl")

def create_world():
    
    #create classes
    
    keywords_arr = get_keywords()
    range_arr = keywords_arr.__len__()
    #print (range_arr)
    #print(keywords_arr)
    aux_arr = []
    
    with onto2:
        with onto3:
            class Theme(onto3['Article']):
                pass
        class Mental_Health(Theme):
            pass
        class has_theme(ObjectProperty):
            domain = [Theme]
            range = [Mental_Health]

        

    for i in keywords_arr:
        if i.__len__() is not 0:
            _str = re.split(r"['(.*?)']", i)
            aux_arr.append(_str[1])
            Mental_Health(_str[1])
            #print (str)

    print(aux_arr)
    
    onto2.save(file="onto_aux_finale.owl", format="rdfxml")
    onto3.save(file="onto_model_article.owl", format="rdfxml")
# Registro de interacao dentre ontologias

# Utiliza-se de diversas classes presentes em root_ontology.owl 
# enquanto expressoes regulares em buscas


# Os diversos termos de busca se encontram nas labels de onto.classes()

def get_keywords():
    
    keywords_arr = []
    aux_arr = []
    aux_dict = {}
    k = 0
    #print(list(onto.classes()))
    for i in onto.classes():
        occurrence = str(i.label)
        aux_arr.append(occurrence)
        _str = re.split(r"['(.*?)']", occurrence)
        aux_dict[k] = _str[1]
        k += 1
        #print(i.label)

 #.lower().split()
        
    return aux_arr

#get_keywords()
create_world()

# Registro de ocorrencias em ambas ontologias
        
# Outros exemplos de anotacoes:

#for i in onto.properties():
#    aux_arr = []
#    aux_arr = i.label[0].lower()
#    print(aux_arr)

#print(list(onto.properties()))
#for i in onto.properties():
    #print(i.label)
    
"""
        afeta
        definidaspor
        por
        tem
        vulneraveisa
        atravesde
        obtém
        provoca
        identificadospor
        possui
        causa
        é
        compostapor

print(list(onto.annotation_properties()))
for i in onto.annotation_properties():
    print(i.label.lower().split())
    
print(list(onto.data_properties()))
for i in onto.data_properties():
    print(i.label)
    
print(list(onto.object_properties()))
for i in onto.object_properties():
    print(i.label)

print(list(onto.individuals()))
for i in onto.object_properties():
    print(i.label[0].lower())
"""