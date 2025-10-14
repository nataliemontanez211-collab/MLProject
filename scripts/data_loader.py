import os
import pandas as pd
import numpy as np

def load_volatility_data(data_path='../data', frequency='5_min'):
    sheet_map = {
        'dates': 'Dates',
        'companies': 'Companies',
        'rv': 'RV_5',
        'bpv': 'BPV_5',
        'good': 'Good_5',
        'bad': 'Bad_5',
        'rq': 'RQ_5'
    }
    
    file = os.path.join(data_path, 'RV_March2024.xlsx')
    
    df_dates = pd.read_excel(file, sheet_name=sheet_map['dates'], header=None)
    df_companies = pd.read_excel(file, sheet_name=sheet_map['companies'], header=None)
    
    date_index = pd.to_datetime(df_dates[0])
    companies = df_companies[0].tolist()
    
    data_frames = {}
    for measure in ['rv', 'bpv', 'good', 'bad', 'rq']:
        sheet_name = sheet_map[measure]
        df = pd.read_excel(file, sheet_name=sheet_name, header=None)
        df.columns = companies
        df.index = date_index
        df.replace(0, np.nan, inplace=True)
        data_frames[measure] = df
        
    return data_frames, date_index, companies
