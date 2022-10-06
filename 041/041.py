def convert_days_to_seconds(days):
    # 1 day = 24 hours
    # 1 hour = 60 minutes
    # 1 minute = 60 seconds
    seconds = days * 24 * 60 * 60
    return seconds


def convert_celsius_to_fahrenheit(celsius_degrees):
    fahrenheit = (celsius_degrees * 9/5) + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit_degrees):
    celsius = (fahrenheit_degrees - 32) * 5/9
    return celsius


def convert_miles_to_kilometers(miles):
    # 1 mile = 1.609344 km
    return miles * 1.609344


def convert_kilometers_to_miles(kilometers):
    return kilometers / 1.609344


if __name__ == "__main__":
    days = int(input("Enter number of days: "))
    print(f"{days} day(s) = {convert_days_to_seconds(days)} seconds")

    deg = u"\u00b0"

    celsius = float(input("Enter Celsius degrees: "))
    print(f"{celsius}{deg} C = {convert_celsius_to_fahrenheit(celsius)}{deg} F")

    miles = int(input("Enter number of miles: "))
    print(f"{miles} miles = {convert_miles_to_kilometers(miles)} km")
