import csv
# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    # for row in data:
    #     print(row)
        
    for colum in data:
        if colum[1] != "temp":
            temp = int(colum[1])
            temperature.append(temp)
    print(temperature)
