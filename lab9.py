import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000))
#
# ts = ts.cumsum()
# print(ts)
#
# ts.plot()
# plt.savefig('stonks.png')
# plt.show()

# data = {'Kraj':['Polska', 'Cos1', 'Cos2','Susland'],'Stolica':['Warszawa','A','B','Amogus'],'Populacja':[1234,456,789,69420],'Kontynent':['Evropa','no','no','the void']}
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
#
# grupa.plot(kind='bar',xlabel='Kontynent',ylabel='Populacja w mln',rot=0, title='Populacja dla 100% legit kontynentów')
#
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Populacja w mln')
# wykres.set_title('Populacja dla 101% legit kontynentów')
# wykres.tick_params(axis='x',labelrotation=0)
# wykres.legend()
# plt.savefig('wykres1.png')
# plt.show()

# df = pd.read_csv('dane.csv',header=0,sep=';',decimal='.')
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# print(grupa)
# grupa.plot.pie(subplots=True,autopct='%.2f %%',fontsize=10,figsize=(6,6),legend=(0,0))
# # y = 'Wartość zamówienia'
# plt.show()
# df = pd.DataFrame(ts)
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend(['Wartości', 'Średnia krocząca'])
# plt.show()

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,header=0)

nic = df.groupby(['Rok']).agg({'Liczba':['sum']})
print(nic)
unik = df['Rok'].unique()

nic.plot()
plt.xticks(unik, rotation=90)
plt.show()
