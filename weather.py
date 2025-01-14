import json
import csv
with open("precipitation.json", 'r', encoding = 'utf-8') as file: 
    precipitation = json.load(file)

monthly_prec = {}
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
for month in months:
    monthly_prec [month] = 0

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

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(monthly_precipitation, file)

total_preci = 0
for labs in precipitation: 
    if (labs ['station'] == 'GHCND:US1WAKG0038'): 
        prep = int(labs['value'])
        total_preci +=prep

total_precipitation = [total_preci]

relative_monthly = {}
for month in months: 
    relative_pre = (monthly_prec[month])/total_preci
    relative_monthly[month] = relative_pre 

results = {}
results = {
    "total_precipitation": total_precipitation,
    "relative monthly precipitation": relative_monthly,
    "monthly_precipitation": monthly_precipitation
}
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4)
