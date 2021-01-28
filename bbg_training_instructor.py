# BBG training instructor
"""
The BBG training instructor is based on KAYLA ITSINES - CLEAN SLATE BBG BEGINNER WORKOUT PROGRAM - WEEK 1
(https://www.refinery29.com/file/13888/ki-bbg-beginner-refinery29-clean-slate-week-1.pdf)
"""

# modules and libraries
import time
import pandas as pd

# program data
bbg_data = "C:/Users/nschn/Documents/python_code/bbg_data.csv"
df = pd.read_csv(bbg_data)

# input and variables
day = input("Please enter the day (number) of your exercise programme and confirm by pressing ENTER:")
while True:
    try:
        value = int(day)
    except ValueError:
        day = input("Please enter a VALID day (number) of your exercise programme and confirm by pressing ENTER:")
        continue
    if not (0 < int(day) < 6):
        day = input("Please enter a VALID day (number) of your exercise programme and confirm by pressing ENTER:")
        continue
    break
day = int(day)

df_line = day-1
selection = df.iloc[df_line]
circuit1 = df.iloc[df_line, 2:6]
circuit2 = df.iloc[df_line, 6:10]
recovery = df.iloc[df_line, 2:10]
rec = df.loc[df_line, "Rest"]


# functions
def countdown(t):
    print("COUNTDOWN:")
    t = int(t)
    while t > -1:
        min, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


def bbg():
    print("\nUp next...\n")
    time.sleep(2)
    for item in circuit1:
        print(item)
    time.sleep(2)
    countdown(7*60)
    print("\nCircuit completed.\n")
    time.sleep(2)
    print("Rest")
    time.sleep(2)
    countdown(30)
    print("\nUp next...\n")
    time.sleep(2)
    for item in circuit2:
        print(item)
    time.sleep(2)
    countdown(7*60)
    print("\nCircuit completed.\n")
    time.sleep(2)


def bbg_recovery():
    print("\nToday's workout is:", df.loc[d, "Workout"])
    print("\nUp next...\n")
    time.sleep(2)
    for item in recovery:
        print(item)
    time.sleep(2)
    print("\nThe recovery workout is finished once all items have been completed.\n")
    time.sleep(2)


print("\nToday's workout is:", df.loc[d, "Workout"])
if rec == "yes":
    bbg()
    print("Rest")
    time.sleep(2)
    countdown(30)
    bbg()
    print("Finished. Well done!")
else:
    bbg_recovery()
    input("Press ENTER once you are done.\n")
    print("Finished. Well done!")
