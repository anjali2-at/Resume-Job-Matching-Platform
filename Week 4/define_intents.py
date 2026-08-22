import pandas as pd

data=pd.read_csv("intents.csv")

print("Intent Dataset")
print(data)

print("\nIntents:")
print(data["intent"].unique())

print("\nNumber of intents:",data["intent"].nunique())

print("\nExamples for each intent:")

for intent in data["intent"].unique():
    print("\n",intent)
    print(data[data["intent"]==intent]["example"].values)