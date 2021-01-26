import datetime
currentDate = input("Enter current date in MM-DD-YY format:\n")
currentDate = datetime.datetime.strptime(currentDate, "%m/%d/%Y").date()
print("Current Day")
print("Month:" + currentDate.strftime('%B'))
print("Day:" + currentDate.strftime('%d'))
print("Year:" + currentDate.strftime('%Y'))

birthday = input("Enter your birthday (MM/DD/YY):\n")
birthday = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
print("Birth Day")
print("Month:" + birthday.strftime('%B'))
print("Day:" + birthday.strftime('%d'))
print("Year:" + birthday.strftime('%Y'))

age = currentDate.year - birthday.year
print('You are', age, 'years old')
if currentDate.day == birthday.day:
    print("Happy Birthday!")



