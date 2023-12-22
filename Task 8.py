import numpy as np
import pandas as pd
headers_data = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", type(headers_data))
df = pd.read_csv('Dataset_1.data',names = headers_data)
print("The first 5 rows of the dataframe")
df.head(5)
df.tail(10)
print(df.dtypes)
df.describe(include = "all")
df.describe(include = "all")
df.replace("?",np.nan,inplace = True)
df.info()
df.to_csv("saved_dataset.csv")
