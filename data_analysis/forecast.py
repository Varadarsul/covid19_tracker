import pandas as pd
import requests
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Fetch historical data for a country (e.g., India)
url = "https://disease.sh/v3/covid-19/historical/India?lastdays=30"
data = requests.get(url).json()

cases = data["timeline"]["cases"]
df = pd.DataFrame(list(cases.items()), columns=["Date", "TotalCases"])
df["Days"] = range(len(df))

X = df[["Days"]]
y = df["TotalCases"]

model = LinearRegression()
model.fit(X, y)

future = pd.DataFrame({"Days": list(range(len(df), len(df) + 7))})
predictions = model.predict(future)

plt.plot(df["Days"], y, label="Actual")
plt.plot(future["Days"], predictions, label="Predicted", linestyle='--')
plt.legend()
plt.title("7-Day COVID Forecast (India)")
plt.xlabel("Days")
plt.ylabel("Total Cases")
plt.show()