# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:29:40 2025

@author: gyusz
"""
import requests, sys, json

import pandas as pd
import numpy as np
# 
params = {
  "fields": [
    "organism_name"
  ]
}
list_all_prot = pd.read_csv(r'C:\Users\gyusz\Downloads\prepared_biolip_win_p_training.csv',  usecols = ['uniprot_id'])
list_human_cross_interacting_prot = pd.read_csv(r'C:\Users\gyusz\Desktop\PPI\all_overlap.csv', delimiter= ';').iloc[:,1]
list_bact_cross_interacting_prot = pd.read_csv(r'C:\Users\gyusz\Desktop\PPI\all_overlap.csv', delimiter= ';').iloc[:,0]
list_human_non_cross_interacting_prot = []
list_bact_non_cross_interacting_prot =[]


human_counter = len(list_human_cross_interacting_prot)
list_bact_species = []
for prot in list_bact_cross_interacting_prot:
    
    base_url = f"https://rest.uniprot.org/uniprotkb/{prot}"
    response = requests.get(base_url, params=params)
    
    try:
        list_spec = response.json()['organism']['scientificName'].split()[0:2]
        
        list_bact_species.append(list_spec[0] + ' ' + list_spec[1])
        
    except:
        break
    

i = 0
while human_counter > 0:
    prot = list_all_prot.iloc[i,0].strip()
    base_url = f"https://rest.uniprot.org/uniprotkb/{prot}"
    i = i + 1
    response = requests.get(base_url, params=params)
    try:
        list_spec = response.json()['organism']['scientificName'].split()[0:2]
    except:
        
        continue
    try:
        species = list_spec[0] + ' ' + list_spec[1]
    except:
        
        continue
    if species == 'Homo sapiens':
       
        if prot not in list_human_cross_interacting_prot.values:
            list_human_non_cross_interacting_prot.append(prot)
            human_counter = human_counter - 1
            print(human_counter)

i = 0
while len(list_bact_species) > 0:
     prot = list_all_prot.iloc[i,0]
     base_url = f"https://rest.uniprot.org/uniprotkb/{prot}"
     i = i + 1
     response = requests.get(base_url, params=params)
     try:
         list_spec = response.json()['organism']['scientificName'].split()[0:2]
     except:
         
         continue
     try:
         species = list_spec[0] + ' ' + list_spec[1]
     except:
         
         continue
     if species in list_bact_species:
         if prot not in list_bact_cross_interacting_prot.values:
             list_bact_species.remove(species)
             list_bact_non_cross_interacting_prot.append(prot)
             print('bact+1', species)
                
            

                
                
            
    
     
    
    