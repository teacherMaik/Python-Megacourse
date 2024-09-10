import csv


with open("files/weather.csv") as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter a city -> ")
city_found = False

for row in data[1:]:
    if row[0] == city:
        print(f"The temperature of {row[0]} is {row[1]}")
        city_found = True

if not city_found:
    print("Don't have that city")
