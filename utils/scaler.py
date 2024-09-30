'''
Scaling values of validation cohort, using the power scaler
'''

import pandas as pd
from sklearn.preprocessing import PowerTransformer

def df_scaler(df:pd.DataFrame, response_column_name=None)-> pd.DataFrame:
    df = df.copy()
    object_only_list = []
    if response_column_name is not None:
        if response_column_name not in df.columns:
            raise Exception('No response column name; please check and set them as response')
    # remove string-only columns, such as surgical number
    for col in df.columns:
      if df[col].dtype == 'object':
          object_only_list.append((col, df[col]))
          df.drop(col, axis='columns', inplace=True)

    transformer = PowerTransformer(method='yeo-johnson')
    if response_column_name is not None:
        df_ = df.drop([response_column_name], axis=1, inplace=False)
    else: df_ = df
    scaled_arr = transformer.fit_transform(df_)
    scaled_df = pd.DataFrame(scaled_arr, columns=df_.columns)
    if response_column_name is not None:
        scaled_df['response'] = df[response_column_name]
    else:pass
    for name, col in object_only_list:
        scaled_df[name] = col
    return scaled_df

