import json
import pandas as pd

df = pd.read_csv('raw_data\student_coffee_crisis.json', sep=";")
# df = pd.json_normalize(data)
print(df.head())
