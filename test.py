import pandas as pd

df =pd.read_csv('pvpc_21_22.csv')
a = df['Hora'].unique()
print (sorted(a))