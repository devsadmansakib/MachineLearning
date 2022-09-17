import pandas
from sklearn.linear_model import LinearRegression

data = pandas.read_csv("iphone_price.csv")

model = LinearRegression()

model.fit(data[["version"]], data[["price"]])

print("Predicted price is ", model.predict([[14]]))
