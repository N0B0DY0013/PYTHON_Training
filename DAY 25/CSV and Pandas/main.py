
# import csv
import pandas

# data = []
# # temperatures = []

# # with open("weather_data.csv", mode = "r") as csv_file:
    
# #     data = csv.reader(csv_file)
    
# #     for row in data:
# #         try:
# #             temperatures.append(int(str(row).split(";")[1]))
# #         except:
# #             pass
    
# # print(data)
# # print(temperatures)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# data = pandas.read_csv("weather_data.csv", sep=";")
# # print(data["temp"])
# temp_series = data["temp"]
# print(f"AVG: {sum(temp_series) / len(temp_series.to_list())}")
# print(f"MAX: {temp_series.max()}")
# print(f"GET ROW OF MAX DAY: \n{data[data['temp'] == temp_series.max()]}")
# print(f"GET TEMP OF MONDAY TO FARENHEIT: {int(data[data['day'] == 'Monday'].iloc[0]['temp']) * 1.8 + 32}")
# # print(data[data['day'] == 'Monday'].iloc[0].temp)
# # print(data.iloc[0])

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

unique_colors = squirrel_data["Primary Fur Color"].unique().tolist()
count_per_color = []

for color in unique_colors:
    count_per_color.append(int(squirrel_data[squirrel_data["Primary Fur Color"] == color]["X"].count()))

print(unique_colors)
print(count_per_color)

squirrel_dict = {"Fur Color": unique_colors,
                 "Count": count_per_color}

pandas.DataFrame.from_dict(squirrel_dict).to_csv("squirrel_count.csv", sep = ";")
