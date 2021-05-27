import pandas as pd
import matplotlib.pyplot as plt

#GR. a
#1
# 1.1
df = pd.read_csv('cars.csv', sep=';', decimal='.')
print(df)
# 1.2
df2 = df[df['Weight'] < 2200]
print(df2)
# 1.3
a = df2.groupby(['Model year'])['Horsepower'].mean()
print(a)
# 1.4
wykres = a.plot.bar('red')
wykres.set_xlabel('Lata')
wykres.set_ylabel('Os y')
plt.xticks(rotation=45)
plt.savefig('obrazek.png')
plt.show()