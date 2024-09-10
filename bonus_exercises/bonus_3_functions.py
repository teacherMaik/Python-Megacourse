def get_average():
    with open('files/data.txt', 'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(temp) for temp in values]

    average_local = sum(values) / len(values)
    return average_local


average = get_average()

print(average)


def greet(message):
    new_message = message.capitalize()
    print("Hey hey ")
    return new_message


user_entry = input("What message do you want to send? -> ")

greeting = greet(user_entry)
print(greeting)


# De-coupling practice
feet_inches = input("How many feet and how many inches? -> ")


def parse(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])
    return {'feet': feet, 'inches': inches}


def convert(feet, inches):
    meters = round(feet * 0.3048 + inches * 0.025, 2)
    return meters


parsed = parse(feet_inches)
converted = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {converted} meter")

if converted > 1.4:
    print("Kid can play on slide")
else:
    print("Kid not tall enough to play on slide")

