import pandas as pd

df = pd.read_csv('raw_data\student_coffee_crisis.csv',
                 sep=";", #different delimiter
                 encoding="utf-8",
                 skiprows=1)
print(df.head())
