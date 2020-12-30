'''Movie Box Office Revenue Prediction'''
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/dasari.shravani/OneDrive - EY/Desktop/Python 3/Udemy/Philipp Muellauer/cost_revenue_clean.csv")
# print(data.head())
# print(data.describe())

X = DataFrame(data,columns = ['production_budget_usd'])  #prod budget
y = DataFrame(data,columns = ['worldwide_gross_usd'])    #gross revenue

'''Visualize'''
plt.figure(figsize=(10,6))
plt.scatter(X, y, alpha=0.3)
plt.title('Film Cost vs Global Revenue')
plt.xlabel('Production Budget $')
plt.ylabel('Worldwide Gross $')
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()
