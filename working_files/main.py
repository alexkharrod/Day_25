import pandas



data = pandas.read_csv("./working_files/weather_data.csv")
my_data = data["temp"].max()
print(my_data)


temperature = data[data.day == "Monday"]
print(temperature.temp)
fahrenheit = (temperature.temp * 1.8) + 32
print(fahrenheit)


# Create a data frame