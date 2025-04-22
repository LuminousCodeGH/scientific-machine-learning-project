import pandas as pd


def decorrelate_window(df: pd.DataFrame) -> pd.DataFrame:
    '''Decorrelate windows. 
    
    Usage: df_decorrelated = decorrelate_windows(df)'''
    for size in [9,7,5,3]:
        if size == 3:
        
            cols_big = df.loc[:,  [col.startswith(str(size)) for col in df.columns]]
            str_list = [str(col)[5:] for col in cols_big.columns]
            cols_small = df.loc[:,  str_list]
        
        else:
            cols_big = df.loc[:,  [col.startswith(str(size)) for col in df.columns]]
            cols_small = df.loc[:,  [col.startswith(str(size-2)) for col in df.columns]]
        
        cols_small.columns = cols_big.columns
        cols_big_corrected = (size*cols_big - (size-2)*cols_small)/2
        df.loc[:,  [col.startswith(str(size)) for col in df.columns]] = cols_big_corrected
    return df
