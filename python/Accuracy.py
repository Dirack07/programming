import pandas as pd
import matplotlib.pyplot as plt

df_acc = pd.read_csv('/home/dirac/programming/python/test.csv', header=0,
                     names=['Fecha', 'Precision_Localizacion', 'Tipo_Localizacion'])
df.plot(x=)
y = df_acc[['Fecha']]
x = df_acc.groupby(by=['Tipo_Localizacion', 'Fecha'])
x['Fecha'].plot()
#import pdb; pdb.set_trace()
#print(x.head(5))