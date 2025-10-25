import os
import pandas as pd
import numpy as np

def load_volatility_data(data_path='../data', frequency='5_min'):
    sheet_map = {
      '1_min': {'rv': 'RV', 'bpv': 'BPV', 'good': 'Good', 'bad': 'Bad', 'rq': 'RQ'},
      '5_min': {'rv': 'RV_5', 'bpv': 'BPV_5', 'good': 'Good_5', 'bad': 'Bad_5', 'rq': 'RQ_5'}
    }

    file = os.path.join(data_path, 'RV_March2024.xlsx')

    df_dates = pd.read_excel(file, sheet_name='Dates', header=None)
    df_companies = pd.read_excel(file, sheet_name='Companies', header=None)

    date_index = pd.to_datetime(df_dates[0], errors='coerce')
    companies = df_companies[0].astype(str).tolist()

    data_frames = {}
    for measure, sheet_name in sheet_map[frequency].items():
      df = pd.read_excel(file, sheet_name=sheet_name, header=None)

      if df.shape[1] > len(companies):
        df = df.iloc[:, :len(companies)]

      df.columns = companies
      df.index = date_index

      df.replace(0, np.nan, inplace=True)

      data_frames[measure] = df

    return data_frames, date_index, companies
  
  
def create_panel_data(data_path='../data', frequency='5_min'):
    sheet_map = {
        "dates": "Dates", "companies": "Companies",
        "rv": "RV_5" if frequency == "5_min" else "RV",
        "bpv": "BPV_5" if frequency == "5_min" else "BPV",
        "good": "Good_5" if frequency == "5_min" else "Good",
        "bad": "Bad_5" if frequency == "5_min" else "Bad",
        "rq": "RQ_5" if frequency == "5_min" else "RQ"
    }
    
    file = os.path.join(data_path, 'RV_March2024.xlsx')
    df_dates = pd.read_excel(file, sheet_name=sheet_map["dates"], header=None)
    df_companies = pd.read_excel(file, sheet_name=sheet_map["companies"], header=None)
    dates_index = pd.to_datetime(df_dates[0], format='%d-%b-%Y')
    company_cols = df_companies[0].tolist() 
    
    stacked_series = []
    for measure in ["rv", "bpv", "good", "bad", "rq"]:
        sheet_name = sheet_map[measure]
        df = pd.read_excel(file, sheet_name=sheet_name, header=None)
        df.columns = company_cols
        df.index = dates_index
        df.index.name = "Date"
        df.replace(0, np.nan, inplace=True)
        
        stacked = df.stack(dropna=False)
        stacked.name = measure
        stacked.index.names = ["Date", "Stock"]
        stacked_series.append(stacked)
    
    panel_df = pd.concat(stacked_series, axis=1)
    return panel_df
