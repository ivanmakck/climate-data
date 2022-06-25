import pandas as pd
import os

data_path = './data'
if not os.path.exists(data_path):
    os.mkdir(data_path)

dfs = []
for filename in os.listdir(data_path):
    filepath = os.path.join(data_path, filename)
    if '.csv' in filename:
        if len(dfs) == 0:
            df = pd.read_csv(filepath, index_col=None)
            dfs.append(df)
        else:
            df = pd.read_csv(filepath, header=0, index_col=None)
            dfs.append(df)

all_years = pd.concat(dfs, ignore_index=True)

output_path = './output'
if not os.path.exists(output_path):
    os.mkdir(output_path)

out_filepath = os.path.join(output_path, 'all_years.csv')
all_years.to_csv(out_filepath, index=False)