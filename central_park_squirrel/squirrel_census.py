import pandas


census = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = census[census["Primary Fur Color"] == "Gray"]

cinnamon_squirrels = census[census["Primary Fur Color"] == "Cinnamon"]

black_squirrels = census[census["Primary Fur Color"] == "Black"]


print(f"Total Gray Squirrels: {len(gray_squirrels)}")
print(f"Total Cinnamon Squirrels: {len(cinnamon_squirrels)}")
print(f"Total Black Squirrels: {len(black_squirrels)}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")