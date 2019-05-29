import datetime
import requests

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
            yield start_date + datetime.timedelta(n)

city="Matiari"
start_date="2014-01-01"
end_date="2019-01-1"
date_format = "%Y-%m-%d"

start_date = datetime.datetime.strptime(start_date, date_format)
end_date = datetime.datetime.strptime(end_date, date_format)

all_data = []
maxtempC_list=[]
maxtempF_list=[]
mintempC_list=[]
mintempF_list=[]


for each_date in daterange(start_date, end_date):
    print(each_date.date())

    ask = str(each_date.date())


    json_data = requests.get(
        'http://api.worldweatheronline.com/premium/v1/past-weather.ashx',
        params=dict(
            key='eeba832fd6c4430c9ca80712192705',
            q=city,
            format='json',
            date=ask,
            tp='24'
        )
    ).json()
    print(json_data)

    all_data.append(json_data)