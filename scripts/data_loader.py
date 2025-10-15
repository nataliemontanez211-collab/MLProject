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
