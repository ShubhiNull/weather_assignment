import json
import csv
with open("precipitation.json", 'r', encoding = 'utf-8') as file: 
    precipitation = json.load(file)

monthly_prec = {}
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
for month in months:
    monthly_prec [month] = 0

location = csv.DictReader(open("stations.csv"))

locations = ["USW00093814",
"US1WAKG0038",
"USC00513317",
"US1CASD0032]


for state in locations: 
    total_preci = 0
    for labs in precipitation:
        for month in months: 
            total_monthly_precipitation = 0
            for labs in precipitation: 
                if (labs ['station'] == 'locations'): 
                    if (f"2010-{month}-01" <= labs['date'] <= f"2010-{month}-31"):
                        prep = int(labs['value'])
                        total_monthly_precipitation += prep
                monthly_prec[month] = total_monthly_precipitation 
        total_monthly_precipitation = 0
        monthly_precipitation = []
        monthly_precipitation.append(monthly_prec[month])
        if (labs ['station'] == 'Station'): 
            prep = int(labs['value'])
            total_preci +=prep
        total_precipitation = [total_preci]
        relative_monthly = {}
        for month in months: 
            total_preci = int(total_preci)
            relative_pre = (monthly_prec[month])/total_preci
            relative_monthly[month] = relative_pre 

results = {}
results ['State'] = {
    "total_precipitation": total_precipitation,
    #"relative monthly precipitation": relative_monthly,
    "monthly_precipitation": monthly_precipitation
}
with open('allresults.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4)


