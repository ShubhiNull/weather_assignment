import json
import csv
with open("precipitation.json", 'r', encoding = 'utf-8') as file: 
    precipitation = json.load(file)

monthly_prec = {}
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
for month in months:
    monthly_prec [month] = 0

with open('stations.csv') as file: 
    locations = list(csv.DictReader(file))

total_precipitation = []
for Station in locations: 
    total_preci = 0
    for labs in precipitation:  
        if (labs ['station'] == Station['Station']):
            prep = int(labs['value'])
            total_preci +=prep
    total_precipitation.append(total_preci)
    relative_monthly = {}
    for month in months: 
        relative_pre = (monthly_prec[month])/total_preci
        relative_monthly[month] = relative_pre
    for month in months: 
        total_monthly_precipitation = 0
    for labs in precipitation: 
        if (labs ['station'] == 'GHCND:US1WAKG0038'): 
            if (f"2010-{month}-01" <= labs['date'] <= f"2010-{month}-31"):
                prep = int(labs['value'])
                total_monthly_precipitation += prep
        monthly_prec[month] = total_monthly_precipitation
    monthly_precipitation = []
for month in months:
    monthly_precipitation.append(monthly_prec[month]) 
monthly_prec = {}
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
for month in months:
    monthly_prec [month] = 0





