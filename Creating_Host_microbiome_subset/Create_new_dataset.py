# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:25:05 2025

@author: gyusz
"""
import pandas as pd
df_non = pd.read_csv(r'C:\Users\gyusz\Desktop\PPI\non_overlap_df.csv', header = 0)
df_overlap = pd.read_csv(r'C:\Users\gyusz\Desktop\PPI\overlap_df.csv', header = 0)
#print(df.iloc[2,4].split(','))

final_df = pd.DataFrame(columns= list(df_non.columns) + ['is_cross_interacting'] + ['aa_ProtPosition'])
rows = []
for k, row in df_non.iterrows():
    for i,_ in enumerate(row.loc['domain'].split(',')):
        new_row = []
        for col in df_non.columns:
            if isinstance(row.loc[col], str):
                
                if ',' in row.loc[col]:
                    new_row.append(row.loc[col].split(',')[i])
                else:
                    new_row.append(row.loc[col])
            else:
                new_row.append(row.loc[col])
        new_row.append('0')
        new_row.append(i+1)
        rows.append(new_row)

for k, row in df_overlap.iterrows():
    for i,_ in enumerate(row.loc['domain'].split(',')):
        new_row = []
        for col in df_non.columns:
            if isinstance(row.loc[col], str):
                if ',' in row.loc[col]:
                    new_row.append(row.loc[col].split(',')[i])
                else:
                    new_row.append(row.loc[col])
            else:
                new_row.append(row.loc[col])
        new_row.append('1')
        new_row.append(i+1)
        rows.append(new_row)
        

final_df = pd.DataFrame(rows, columns=list(df_non.columns) + ['is_cross_interacting'] + ['aa_ProtPosition'])
final_df.to_csv(r'C:\Users\gyusz\Desktop\PPI\new_dataset.csv', index = False)
                
                
                
    