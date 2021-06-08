#### Importing Pandas and others and Reading csv file
import os
import matplotlib.pyplot as plt
import math
import numpy as np
import seaborn as sns
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

##Remodified .CSV data to make managing data easier.
##Some data cleaning.
Cardano = pd.read_csv('Cardano.csv')

##Created A daily Average for each day to work around with the data.
Cardano['Daily Average'] = Cardano.iloc[:, 2:4].sum(axis=1)/2

##Just to let the viewer see the data that is coming out, truancated
##because there is 2843 rows to show.... too much data, lol
print(Cardano[['Date', 'Low', 'High', 'Daily Average']])
print(Cardano[['Date', 'Open', 'Close']])
print(Cardano[['Date', 'Volume', 'Market Cap']])


#Line graph plot to show, low, high, and Average price
Cardano.plot(x="Date", y=["Low", "High", "Daily Average"], figsize=(15, 20), title ="Cardano Low, High, and Daily Average Prices.", ylabel="Price in $")
plt.show()

#Line graph to show traditonal Open and Close (although the selling and buying never sleeps for Cryptocurrency)
Cardano.plot(x="Date", y=["Open", "Close"], figsize=(15, 30), title ="Open and Close Prices.", ylabel="Price in $")
plt.show()

#Line graph to Show Volume and Market Cap
#These two indicators are important to understand how healthy or not healthy a particular stock or cryptocurrency is.
#High Volume but decrease in price could mean people are because they see a decrease in price or cashing out
#High Volume and higher price means that people are still buying the currency because there is value.
Cardano.plot(x="Date", y=["Volume", "Market Cap"], figsize=(15, 50), title ="Volume and Market Cap.", ylabel="Price in $ (10B)")
plt.show()

#line graph plot to show, low, high, and Average price
Cardano.plot(x="Date", y=["Low", "High", "Daily Average"], figsize=(15, 20), title ="Cardano Low, High, and Daily Average Prices.", ylabel="Price in $")

plt.ylim([0, 2])
plt.xlim([1500, 2000])
plt.xticks(visible = True)
plt.show()

Cardano['Date'] = pd.to_datetime(Cardano['Date']).apply(lambda date: date.toordinal())

X = Cardano[["Date"]]
y = Cardano[["Daily Average"]]

regressor = LinearRegression()
regressor.fit(X, y)

y_pred = regressor.predict(X)

plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('Simple Cardano Regression')
plt.xlabel('Ordinal Date')
plt.ylabel('Daily Average Price in $')
plt.figsize=(15, 30)
plt.show()
