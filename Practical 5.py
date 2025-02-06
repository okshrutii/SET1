#PRACTICAL 5
#AIM: A program that checks if a given year is a leap year.
def is leap year (year):
if (year % 40 and year % 100 != 0) or (year % 400 == 0):
return True
else:
return False
input year int (input("Enter a year: "))
if input year <= 0:
raise ValueError ("Please enter a valid positive year.")
if is_leap_year(input_year):
print("{) is a leap year.".format(input_year))
else:
print("() is not a leap year.".format(input_year))
