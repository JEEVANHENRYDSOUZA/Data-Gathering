import pandas as pd

df=pd.read_json('https://api.exchangerate-api.com/v4/latest/INR')
print(df)
