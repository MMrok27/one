import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5.5, np.nan, 'a'])
# print(s)
s1 = pd.Series([12, 12, 8, 14], index=['a', 'b', 'c', 'd'])
# print(s1)
dane = {'Kraj':['Polska', 'Cos1', 'Cos2'],'Stolica':['Warszawa','A','B'],'Populacja':[123,456,789]}

df = pd.DataFrame(dane)
# print(df)
#
# daty = pd.date_range('20220420', periods=5)
# print(daty)
# df2 = pd.DataFrame(np.random.randn(5,4),index=daty,columns=list('ABCD'))
# print(df2)
#
# df3 = pd.read_csv('iris.csv',header=0,sep=',',decimal='.')
# print(df3)
# # df3.to_csv('nowy.csv',index=False)
#
#
# xlsx = pd.ExcelFile('wyniki.xlsx')
# df4 = pd.read_excel(xlsx,header=0)
# print(df4)
# df4.to_excel('nowy.xlsx',sheet_name='arkusz1',index=False)

# print(s1['a'])
# print(s1.a)
# print(df['Stolica'])
# print(df.Kraj[[0]])
# print(df.loc[[0],['Kraj']])
# print(df.at[0, 'Kraj'])
# print('Kraj: '+ df.Kraj)
# print(df.sample(1))
# print(df.sample(frac=0.5))

# print(df.sample(10,replace=True))
# print(df.head())
# print(df.head(2))
#
# df3 = pd.read_csv('iris.csv',header=0,sep=',',decimal='.')
# print(df3.head(10))
# print(df3.tail(10))

# print(s1[(s1 > 9)])
# print(s1.where(s1 > 10, 'element za maly'))
# # seria = s1.copy()
# # seria.where(seria > 10, 'element za maly', inplace=True)
# # print(seria)
#
# print(s1[~(s1 > 9)])
# print(s1[(s1 > 9) & (s1 < 13)])
# print(df[df['Populacja']>500])
# print(df[((df.Populacja < 500) & (df.index.isin([0,2])))])
# szukaj = ['cos1', 'b']
# print(df.isin(szukaj))

s1['e'] = 15
print(s1)

df.loc[3] = 'nowy element'
df.loc[4] = ['Susland','Amogus',69420]
print(df)
df.drop([3], inplace=True)
print(df)
# df.drop('Kraj', axis=1, inplace=True)
df['Kontynent'] = ['Evropa','xqcL','xqcL','the void']
print(df)

print(df.sort_values(by='Kraj'))
grupa = df.groupby(['Kontynent'])
print(grupa.get_group('xqcL'))

print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))

import numpy as np
import pandas as pd
#1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,header=0)
print(df)
#2
print(df[df['Liczba']>1000])
print(df[df['Imie']=='MICHAŁ'])
print(df.agg({'Liczba':['sum']}))

print(df[((df.Rok > 1999) & (df.Rok < 2005))].agg({'Liczba':['sum']}))
print(df.groupby(['Plec']).agg({'Liczba':['sum']}))


print(df.sort_values(by='Liczba',ascending=False).groupby(['Plec']).head(1))

print(df.sort_values(by='Liczba',ascending=False).groupby(['Plec']).head(1))




