import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
import datetime as dt

#Input & Init
print(f'Cypto Currency Analyzer v1 by @yogijr5 \n')
currency = input("Masukkan Kode Mata Uang ex. [USD]: ")
metric = "Close"


start = dt.datetime(2018,1,1)
end = dt.datetime.now()


crypto = ['BTC', 'ETC', 'LTC', 'XRP', 'DASH', 'SC']
colnames = []


#Algoritma & Logika 
first = True
for ticker in crypto:
    data = web.DataReader(f'{ticker}-{currency}', "yahoo", start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames

#Korelasi Fluktuasi Data Crypto
#plt.yscale('log')
#
#for ticker in crypto:
#    plt.plot(combined[ticker], label=ticker)
#
#plt.legend(loc="upper right")


combined = combined.pct_change().corr(method="pearson")
sns.heatmap(combined, annot=True, cmap="coolwarm")

plt.show()