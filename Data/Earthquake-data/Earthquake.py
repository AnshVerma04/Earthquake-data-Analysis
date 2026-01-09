import requests
import pandas as pd

url = "https://raw.githubusercontent.com/MainakRepositor/Datasets/refs/heads/master/earthquakes.csv"

res = requests.get(url)

with open("Earthquake_data.csv", "wb") as file:
    file.write(res.content)

df = pd.read_csv("Earthquake_data.csv")
print(df.head())