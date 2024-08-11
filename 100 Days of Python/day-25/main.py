# reading in CSVs
import csv
import pandas as pd
# data = open("weather_data.csv", "r")
# print(data.readlines())
# data = csv.reader(data)
# for row in data:
#     print(row)
# for temp in data:
#     print((temp[1]))
# print(data)
# data = pd.read_csv("weather_data.csv")
# # print(data)
# print(data['temp'].mean())

# count number of squirrels by squirrel color
# using pandas, perform a group_by() and then count the number of squirrels by squirrel color
# use the summarise() command from R to produce a new data frame with as many observations there are unique colors in the original data frame
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(data.groupby('Primary Fur Color').count())