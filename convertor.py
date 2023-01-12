import pandas as pd

def Convertor(path,name):
    data = pd.read_excel(path,sheet_name=name)
    data.to_csv(f'{name}.csv',index=False,header=True)
    return