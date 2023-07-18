import pandas
# with open("weather_data.csv") as data:
#     all_data=data.readlines()
#     all_data.str
#     print(all_data)

# import csv


# with open("weather_data.csv") as data:
#     all_data=csv.reader(data)
#     next(all_data)
#     temperatures=[]
#     for datas in all_data:
#         temperatures.append(int(datas[1]))
#     print(temperatures)





# data=pandas.read_csv("weather_data.csv")
# data_dict=data.to_dict()
# temp_list=data["temp"].tolist()
# print(data["temp"].max())
# print(data["temp"].mean())
# print(sum(temp_list)/len(temp_list))

# print(data[data["temp"]==data["temp"].max()])

# monday=data[data["day"]=="Monday"]
# monday*=33.8
# print(monday["condition"])

# monday=data.at[0, "temp"]
# monday=(9/5)*(monday)+(32)
# print(monday)

# data_dict={
#     "names": ["Ali", "Hakkı", "Birsen"],
#     "scores": [100, 200, 300]
# }

# data=pandas.DataFrame(data_dict)
# data.to_csv("names.csv")






data=pandas.read_csv("squirell.csv")

fur_colors=data["Primary Fur Color"].tolist()

gray=0
black=0
cinnamon=0


for fur_color in fur_colors:
    if fur_color=="Gray":
        gray+=1
    elif fur_color=="Black":
        black+=1
    elif fur_color=="Cinnamon":
        cinnamon+=1

fur_counts={
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray,black,cinnamon]
}

# squirells=pandas.DataFrame(fur_counts)
# squirells.to_csv("Squirell Fur Count.csv")


a=pandas.read_csv("Squirell Fur Count.csv")
print(a)
