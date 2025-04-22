# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:58:32 2025

@author: gyusz
"""

import requests
import json
import pandas as pd
import time

df = pd.read_excel(r'C:\Users\gyusz\Downloads\13059_2022_2643_MOESM4_ESM.xlsx')

list_all_bact_prot = []
proteins = df.iloc[:,1].unique()
next_url = 1
for protein in proteins:
   
    protein_str = str(protein)  # Convert list to comma-separated string
    
    
    try:
        
        params = {
            "id" : protein_str.strip(),
          "facetFilter": "member_id_type:uniprotkb_id",
          "size": "500",
          
        }
        headers = {
          "accept": "application/json"
        }
        base_url = f"https://rest.uniprot.org/uniref/%7Bid%7D/members"
        
        response = requests.get(base_url, headers=headers, params=params)
            
        print(response)
        for cluster in response.json()['results']:
            list_all_bact_prot.extend(cluster['accessions'])
        print('good', protein_str)
        
        
        
        while True:
            try:
                next_url = response.headers['Link'].split(';')[0][1:-1]
            except:
                break
            i = 0
                
            response = requests.get(next_url.strip())
            if response.status_code != 200:
                break
            dictionary = response.json()
            for cluster in dictionary.get('results', []):
                list_all_bact_prot.extend(cluster['accessions'])
            
            i = i+1
            print(i)
        
    except:
        print('issue with protein', protein_str, )
        continue
            #UniRef50_Q8Y495
        
        


series = pd.Series(pd.Series(list_all_bact_prot).unique())
series.to_csv(r'C:\Users\gyusz\Desktop\list_all_bact.csv')


