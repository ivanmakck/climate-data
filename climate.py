import pandas as pd
import os
import glob

paths = {
    'data_path': './data',
    'output_path': './output'
}

for path in paths.values():
    if not os.path.exists(path):
        os.mkdir(path)

csvs = glob.glob(os.path.join(paths['data_path'], '*.csv'))
out_filepath = os.path.join(paths['output_path'], 'all_years.csv')

dfs = []
for csv in csvs:
    if len(dfs) == 0:
        df = pd.read_csv(csv, index_col=None)
        dfs.append(df)
    else:
        df = pd.read_csv(csv, header=0, index_col=None)
        dfs.append(df)

all_years = pd.concat(dfs, ignore_index=True)
all_years.to_csv(out_filepath, index=False)