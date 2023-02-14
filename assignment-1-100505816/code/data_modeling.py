import pandas as pd

data_path = r"C:\Users\aghazal\Documents\Aalto\Big data\big-data-platfroms-assingments\data\yellow_tripdata_2022-01.parquet"

df = pd.read_parquet(data_path)

print( df.columns )
print ("----------")
print( len(df))
