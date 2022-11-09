import pandas as pd

df = pd.read_csv('iris.csv')

print("shape:",df.shape)
print("*********")
print("First five rows")
print(df.head())
print("*********")
print("Last five rows")
print(df.tail())
print("*********")
print("Size:",df.size)
print("*********")
print("no of samples available for each variety:\n",df["variety"].value_counts())
print("*********")
print("Description:")
print(df.describe())