#### Importing Pandas and others and Reading csv file
import os
import matplotlib.pyplot as plt
import math
import numpy as np
import seaborn as sns
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

##Remodified .CSV data to make managing data easier.
##Some data cleaning.
Bitcoin = pd.read_csv('HistoricalData4.csv')

##Created A daily Average for each day to work around with the data.
Bitcoin['Daily Average'] = Bitcoin.iloc[:, 2:4].sum(axis=1)/2

##Just to let the viewer see the data that is coming out, truancated
##because there is 2843 rows to show.... too much data, lol
print(Bitcoin[['Date', 'Low', 'High', 'Daily Average']])
print(Bitcoin[['Date', 'Open', 'Close']])
print(Bitcoin[['Date', 'Volume', 'Market Cap']])


#Line graph plot to show, low, high, and Average price
Bitcoin.plot(x="Date", y=["Low", "High", "Daily Average"], figsize=(15, 20), title ="Bitcoin Low, High, and Daily Average Prices.", ylabel="Price in $")
plt.show()

#Line graph to show traditonal Open and Close (although the selling and buying never sleeps for Cryptocurrency)
Bitcoin.plot(x="Date", y=["Open", "Close"], figsize=(15, 30), title ="Open and Close Prices.", ylabel="Price in $")
plt.show()

#Line graph to Show Volume and Market Cap
#These two indicators are important to understand how healthy or not healthy a particular stock or cryptocurrency is.
#High Volume but decrease in price could mean people are because they see a decrease in price or cashing out
#High Volume and higher price means that people are still buying the currency because there is value.
Bitcoin.plot(x="Date", y=["Volume", "Market Cap"], figsize=(15, 50), title ="Volume and Market Cap.", ylabel="Price in $ (100B)")
plt.show()

#line graph plot to show, low, high, and Average price
Bitcoin.plot(x="Date", y=["Low", "High", "Daily Average"], figsize=(15, 20), title ="Bitcoin Low, High, and Daily Average Prices.", ylabel="Price in $")

plt.ylim([1000, 20000])
plt.xlim([1500, 2000])
plt.xticks(visible = True)
plt.show()

Bitcoin['Date'] = pd.to_datetime(Bitcoin['Date']).apply(lambda date: date.toordinal())

X = Bitcoin[["Date"]]
y = Bitcoin[["Daily Average"]]

regressor = LinearRegression()
regressor.fit(X, y)

y_pred = regressor.predict(X)

plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('Simple Bitcoin Regression')
plt.xlabel('Ordinal Date')
plt.ylabel('Daily Average Price in $')
plt.figsize=(15, 30)
plt.show()
