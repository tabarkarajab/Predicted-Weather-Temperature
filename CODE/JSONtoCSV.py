import pandas as pd
import simplejson as json

data_file = open("fiveyearsdata.json", "r") 
data = json.load(data_file)
data = data

print("Data size:", len(data), "observations")
df = pd.DataFrame()
for i, d in enumerate(data[:]): # Going through data: observation by observation per each day
    try:
        df_1 = pd.DataFrame(d["data"]["weather"], index=[i])
        df_2 = pd.DataFrame(d["data"]["request"], index=[i])
        df_ = pd.concat([df_1, df_2], axis=1)
        for k, v in d["data"]["weather"][0]["hourly"][0].items():
            df_.loc[i, k] = v
        for k, v in d["data"]["weather"][0]["astronomy"][0].items():
            df_.loc[i, k] = v

        df = df_ if df.empty else df.append(df_)
    except:
        # There are some errors found in fetched data already. 
        # Days missed as a result of an error should be imputed by some way
        print("Error at index:", i, "Error details:", d["data"]) 

df = df.drop('hourly', 1)
df = df.drop('astronomy', 1)

print("Fetched data sieze:", len(df), "observations")
print("Number of variables:", len(df.columns))

df.to_csv('weather_data.csv', sep='|') # sep here is to avoid "," in the query column