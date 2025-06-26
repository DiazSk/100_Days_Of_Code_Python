import pandas as pd

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv 

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))

# print(temperatures)


# data = pd.read_csv("weather_data.csv")

# print(data["temp"])

# temp_list = data["temp"].to_list()

# print(temp_list)

# # Get Mean, Max, Min
# print(data["temp"].mean())

# print(data["temp"].max())

# print(data.temp.min())

# # Get Data in Column
# print(data.day)

# # Get Data in Row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# # 
# monday = data[data.day == "Monday"]

# print(monday.condition)

# monday_temp_c = monday.temp[0] 

# monday_temp_f = monday_temp_c * 9/5 + 32

# print(monday_temp_f)


# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# df = pd.DataFrame(data_dict)
# print(df)

# df.to_csv("new_data.csv")


# Create a dataframe from the squirrel dataset

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_color_data = squirrel_data["Primary Fur Color"].value_counts().to_frame()

squirrel_color_data.to_csv("squirrel_color_data.csv", index=True)



