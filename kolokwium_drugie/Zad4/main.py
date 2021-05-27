import pandas as pd
import matplotlib.pyplot as plt

#zad4
#gr.A

dane = pd.read_csv('cars.csv', sep=';')
dataframka = pd.DataFrame(dane)
dataframka2 = dataframka[dataframka['Car name'].str[:4] == 'ford']
print(dataframka2)
grouped_df = dataframka2.groupby(['Car name'])['Cylinders'].sum()
plt.figure(figsize=(10, 8))
grouped_df.plot.pie(subplots=True, autopct='%.2f %%', fontsize=14, shadow=True)
plt.title("Procentowa ilosc cylindrow w samochodach marki Ford")
plt.legend(loc='lower left')

plt.show()

