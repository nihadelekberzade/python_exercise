import datetime

name = input('Your name : ')
age = float(input('Your age : '))

current_year = datetime.datetime.now().year
goal_year = current_year + (100 - age)
print('100 age year is : ' + str(goal_year))