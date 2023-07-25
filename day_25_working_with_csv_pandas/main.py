
# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv # for reading csv files
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

'''
# to work with csv, excel files pandas will be the best
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)   # get temp column values
# print(data["temp"])
# data_dict = data.to_dict()  # convert table into set of dictionaries
# # print(data_dict)  

# temp = data["temp"].to_list()   # convert a series column to a list
# print(temp)
# avg = data["temp"].mean()   # get average of a series column
# print(avg)

# maxi = data["temp"].max()   # get maximum value of a series column
# print(maxi)

#----------------------------------------------------------------
# note : we can call data.day also and data["day"] also. both are running to access file values
# if we give data.day i.e column name then we will get whole column values
# if we give some filter condition inside data[data.day == "Monday"] then it will fetch row values  
# fetch the row in the table
# print(data[data.day == "Monday"])

# # fetch the row where temperature is maximum
# print(data[data.temp == data.temp.max()])

# get monday temperature in fahrenheit
# monday = data[data.day == "Monday"]
# fahrenheit = (int(monday.temp) * 9/5) + 32
# print(fahrenheit)

# create csv file using DataFrame class under pandas library
data_dict = {
    "students" : ["vishal", "raju","sonu"],
    "scores" : ["23","54","65"]
}
data = pandas.DataFrame(data_dict)
# print(data[data.students == 'vishal'])    # fetch the row
data.to_csv("new_data.csv")# create new csv file with the data_dict values
'''
# ---------------------------- day 25 project -------------------------
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_list = data["Primary Fur Color"].tolist()

data_dict = {
    "color" : ["gray", "Cinnamon", "black"],
    "count" : [color_list.count("Gray"), color_list.count("Cinnamon"), color_list.count("Black")]
    }

squirrel_count = pandas.DataFrame(data_dict)    # create a table in python pandas
print(squirrel_count)
squirrel_count.to_csv("squirrel_count.csv")
