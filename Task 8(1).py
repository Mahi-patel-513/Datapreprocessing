import pandas as pd
import numpy as np
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df = pd.read_csv('car_dataset.data', names = headers)
df.head()
df.replace("?", np.nan, inplace = True)
df.head(5)
missing_data = df.isnull()
missing_data.head(5)
for column in headers:
    print(column)
    print (missing_data[column].value_counts())
    print("")
print(df.dtypes)
avg_nor_loss = df['normalized-losses'].astype("float").mean()
print(avg_nor_loss)
df['normalized-losses'].replace(np.nan, avg_nor_loss,inplace = True)
avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)
df["bore"].replace(np.nan, avg_bore,inplace = True)
avg_bore=df['stroke'].astype('float').mean(axis=0)
print("Average of stroke:", avg_bore)
df["stroke"].replace(np.nan, avg_bore, inplace=True)
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)
df['num-of-doors'].value_counts()
df['body-style'].value_counts().idxmax()
df["num-of-doors"].replace(np.nan, "four", inplace=True)
df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
missing_data = df.isnull()
missing_data.head(5)

for column in headers:
    print(column)
    print (missing_data[column].value_counts())
    print("")

#from sklearn.impute import SimpleImputer
#imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
#imputer.fit(df[['normalized-losses','stroke','bore','horsepower','peak-rpm']])
#df[['normalized-losses','stroke','bore','horsepower','peak-rpm']] = imputer.transform(df[['normalized-losses','stroke','bore','horsepower','peak-rpm']])
#imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
#imputer.fit(df[['num-of-doors']])
#df[['num-of-doors']] = imputer.transform(df[['num-of-doors']])
df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")
df.info()
