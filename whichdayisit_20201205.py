# WhichDayIsIt?

# packages

import math, re

# functions

def delay():
    i=1
    while i<5000000:
        i=i+1

def day_calculation():
    date=input("Please enter a date in the format dd/mm/yyyy:\n")
    while not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",date):
        date=input("Please enter a valid date in the format dd/mm/yyyy:\n")   
    date_list=date.split("/")
    day=int(date_list[0])
    month=int(date_list[1])-1
    year=int(date_list[2])

    months=(31,28,31,30,31,30,31,31,30,31,30,31)
    days=day+sum(months[0:month])
    days_total=((year-1)*365.25)-(((year-1)%4)*0.25)-math.floor(year/100)+math.floor(year/400)+days
    if year%4==0 and month>0:
        days_total=int(days_total+1)
    dayofweek=int(days_total%7)
    weekdays=("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    print(f"This is a {weekdays[dayofweek]}!")

# start

print("""Hi! Want to find out which day of the week a specific date was or will be?
I can help you with that!""")
delay()
print("Now please enter your credit card details:")
delay()
print("Just kidding! I've been told, I have a great sense of humour.")
delay()

day_calculation()

repeat=input("Would you like to check another date? Please enter yes or no:\n")
while True:
    if repeat.lower()!="yes" and repeat.lower()!="no":
        repeat=input("Please enter yes or no:\n")  
        continue
    elif repeat.lower()=="yes":
        day_calculation()
        repeat=input("Would you like to check another date? Please enter yes or no:\n")
        continue
    if repeat.lower()=="no":
        print("No worries! Have a nice day")
        break
