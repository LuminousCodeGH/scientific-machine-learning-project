# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:47:29 2025

@author: gyusz
"""

import pandas as pd
import numpy as np

list_all_prot = pd.read_csv(r'C:\Users\gyusz\Downloads\prepared_biolip_win_p_training.csv',  usecols = ['uniprot_id'])

list_non_overlap = pd.read_csv(r'C:\Users\gyusz\Desktop\PPI\non_overlap.csv', delimiter = ';').values.flatten().tolist()
list_overlap = pd.read_csv(r'C:\Users\gyusz\Desktop\PPI\all_overlap.csv', delimiter = ';').values.flatten().tolist()



indexes_non =np.append(np.where(np.isin(list_all_prot, list_non_overlap))[0] ,-1 ) + 1
indexes_overlap = np.append(np.where(np.isin(list_all_prot, list_overlap))[0], -1) + 1

non_overlap_df = pd.read_csv(r'C:\Users\gyusz\Downloads\prepared_biolip_win_p_training.csv', header = 0, skiprows= lambda x: x not in indexes_non )
overlap_df = pd.read_csv(r'C:\Users\gyusz\Downloads\prepared_biolip_win_p_training.csv', header = 0 , skiprows= lambda x: x not in indexes_overlap)


non_overlap_df.to_csv(r'C:\Users\gyusz\Desktop\PPI\non_overlap_df.csv', index = False)
overlap_df.to_csv(r'C:\Users\gyusz\Desktop\PPI\overlap_df.csv', index = False)