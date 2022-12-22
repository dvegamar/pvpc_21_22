# This is a Python script that takes files of PVPC energy prices from
# https://www.esios.ree.es/es/descargas?date_type=publicacion&start_date=22-12-2022&end_date=22-12-2022
# Files are xls. Cleans the files and takes the prices of all the xls files to build a single csv file with the
# data-hour-price information
import glob, os
import pandas as pd
import xlrd


def clean_xls (xls):
    wb = xlrd.open_workbook_xls(xls, logfile=open(os.devnull, 'w'))
    df_day = pd.read_excel(wb, sheet_name='Tabla de Datos PCB')
    df_day = df_day.iloc [4:, [0, 1, 4]]
    df_day.columns = ['Fecha', 'Hora', 'Precio']
    df_day = df_day.dropna (axis=0, how='any')
    return df_day

files = glob.glob ('pvpc_21_22/PVPC_DETALLE_DD*.xls')
df_total = clean_xls(files[0])
for i in range (1, len(files)):
    last_df = clean_xls (files[i])
    df_total = pd.merge (df_total, last_df, how='outer')

df_total.to_csv('pvpc_21_22.csv', encoding='utf-8', index=False)


print (df_total.info())
print (df_total.unique())



