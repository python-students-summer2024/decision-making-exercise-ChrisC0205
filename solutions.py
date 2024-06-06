"""
A few decision-making puzzles to solve using if/elif/else logic.
Do not call any of these functions from within this file... only do that by running the main.py file.
Your job is to complete the definitions of each function so that it achieves its indicated behavior.
"""

import math
import datetime


def get_year():
    """
    This function is given to you... it is used by the is_leap_year() function below.
    Do not modify this function.
      :returns: The current year, e.g. 2020
    """
    now = datetime.datetime.now()  # get the current time now
    year = now.year  # the current year
    return year


def is_square():
    """
    Asks the user to enter the width and height of an area in inches and determines whether it is square.
    Users can enter either integers or floating point numbers.

      :returns: True if square (i.e. if equal length and height), False otherwise.
    """
    height = input('What is the height of the shape in inches? ')
    length = input ('What is the length of the shape in inches? ')
    height = int(height)
    length = int(length) 
    if height == length:
        return True
    elif height!= length:
            return False
    else:
        print('Please enter a number only ')
        return None
        


def get_greatest():
    """
    Asks the user for two integers, and returns the number that is greatest, as an int.
    You are not allowed to use Python's builtin max() function for this.
    If both numbers are the same, return that number.

    :returns: the greatest of the two input numbers, as an int.
    """
    number_1= input('Give me a number, any number ')
    number_2= input('Give me a second number ')
    if number_1.isnumeric() and number_2.isnumeric():
        number_1 = int(number_1)
        number_2 = int(number_2)
        if number_1>number_2:
            return number_1
        elif number_2>number_1:
            return number_2
        elif number_1==number_2:
            return number_1
    else:
        print('I asked for numbers... ')
        return None


def get_bmi_category():
    """
    Asks the user to enter their height (in inches) and weight (in pounds), in that order, and then returns the user's BMI statistical category.
    Users can enter either integers or floating point numbers.

    The BMI formula was developed in the 1830s, and is still widely used today in public health policy, medical practice, and legislation.
    The formula for calculating BMI is 703 * weight / height^2.
    The BMI statistical categories are:
    - Very severely underweight (BMI < 15)
    - Severely underweight (15 <= BMI < 16)
    - Underweight (16 <= BMI < 18.5)
    - Normal (18.5 <= BMI < 25)
    - Overweight (25 <= BMI < 30)
    - Moderately obese (30 <= BMI < 35)
    - Severely obese (35 <= BMI < 40)
    - Very severely obese (BMI >= 40)

      :returns: The name of the BMI statistical category, based on the inputted height and weight.
    """
    height = input('What is your height in inches? ')
    weight = input('What is your weight in pounds? ')
    if height.isnumeric() and weight.isnumeric():
        height = int(height)
        weight = int(weight)
        the_categories = ['Very severely underweight','Severely underweight','Underweight','Normal','Overweight','Moderately obese','Severely obese','Very severely obese']
        the_bmi = 703 * weight / height ** 2
        if the_bmi < 15:
            return the_categories[0]
        elif 15 <= the_bmi < 16:
            return the_categories[1]
        elif 16<= the_bmi < 18.5:
            return the_categories[2]
        elif 18.5<= the_bmi < 25:
            return the_categories[3]
        elif 25<=the_bmi<30:
            return the_categories[4]
        elif 30 <= the_bmi < 35:
            return the_categories[5]
        elif 35<= the_bmi<40:
            return the_categories[6]
        elif 40<=the_bmi:
            return the_categories[7]
    else:
        return None
  


def get_discount():
    """
    Imagine this scenario: a surgical mask distributor will give you a 20% discount on orders of 5000 or more.
    Each mask individually costs $5.
    This function asks the user how many masks they would like, and returns the total cost after applying any relevant discount
    The total cost must be rounded to the nearest integer and formatted as in "$4,000".

      :returns: The cost of the masks, after any discounts, e.g. "$4,000" for 1000 masks.
    """
    masks = input("How many masks would you like to purchase? ")
    masks = int(masks)
    if masks < 5000:
          masks=(masks*5)
          price= format(int(masks), ',')
          return "$" + str(price)
    elif masks >= 5000:
          masks_1=(masks*5)
          masks_2 = masks_1 -(masks_1*.2)
          price = format(int(masks_2), ',')
          return "$" + str(price)
    else:
        return None


def is_leap_year():
    """
    Determines whether the current year is a leap year.
    Any year evenly divisible by 4 is a leap year, except century years such as 1900, 2000, 2100, etc. Only century years evenly divisible by 400 are leap years.

    :returns: True if the current year is a leap year, False otherwise.
    """
    year = (
        get_year()
    )  # this line is given to you - the variable, year, holds the current year
    #### write your solution for this function below here. ####

    if int(year)%4 is 0:
        return True
    else:
        return False