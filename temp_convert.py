#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Nov 24 2022
# This program converts the temp in celsius to fahrenheit.


def calculate_fahrenheit():
    # get a temperature from the user in  celsius
    temp_celsius_string = input("Enter the temperature (°C): ")
    print("")

    try:
        # converts string to float
        temp_celsius_float = float(temp_celsius_string)
        # convert from celsius to fahrenheit
        temp_fahrenheit = (9 / 5) * temp_celsius_float + 32
        print(
            "{0:,.2f}°C is equal to {1:,.2f}°F".format(
                temp_celsius_float, temp_fahrenheit
            )
        )

    # checks if the number is a string
    except Exception:
        print("{} is not a number.".format(temp_celsius_string))


def main():
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
