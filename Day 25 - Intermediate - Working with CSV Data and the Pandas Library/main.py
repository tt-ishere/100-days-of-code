# import csv
# # with open("weather_data.csv") as weather_data:
# #     data = weather_data.readlines()

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     # for row in data:
#     #     print(row)
        
#     for colum in data:
#         if colum[1] != "temp":
#             temp = int(colum[1])
#             temperature.append(temp)
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data)) #Dataframe
# print((type(data['temp']))) #series 

# data_dict = data.to_dict() #convert weather data to dictionary
# print(data_dict)

# temp_list = data.temp.to_list() #convert temperatures to list
# print(temp_list)

# # average temperature
# average_temp = sum(data.temp) / len(data.temp)
# print(round(average_temp, 2))

# # OR  you can use the mean method of panda to find the average
# average = data.temp.mean()
# print(average)

# max_temp = data.temp.max()
# print(f"Max Temperature: {max_temp}")

# # get data colums in dataframe
# print(data['temp'])
# print(data.temp)

# # get data of rows in dataframe
# print(data[data.day == 'Thursday'])

# # get row of data with the highest temperature
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# mon = data[data.day == "Monday"]
# mon_temp_fahrenheit = (mon.temp * (9 / 5)) + 32 #converting mondays temp to fahrenheit
# print(mon_temp_fahrenheit)

# # creating dataframes from scratch 
# data_dict = {
#     'Students': ['Amy', 'James', 'Enoch'],
#     'Marks': [76, 91, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

# g, c, b

s_data = pandas.read_csv('Squirrel_data.csv')
# print(s_data['Primary Fur Color'])

gray_lenght = len(s_data[s_data['Primary Fur Color'] == "Gray"])

Cinnamon_lenght = len(s_data[s_data['Primary Fur Color'] == "Cinnamon"])

Black_lenght = len(s_data[s_data['Primary Fur Color'] == "Black"])

Fur_color = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_lenght, Cinnamon_lenght, Black_lenght]
}

fur_count = pandas.DataFrame(Fur_color)
fur_count.to_csv("fur_color_count.csv")
