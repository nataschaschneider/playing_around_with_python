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
day = input("Please enter the day (number) of your exercise programme and confirm by pressing ENTER:\n")
while isinstance(day, str):
    try:
        int(day)
    except ValueError or False:
        day = input("Please enter a VALID day (number) of your exercise programme and confirm by pressing ENTER:")
        continue
    if not 0 < int(day) < 6:
        day = input("Please enter a VALID day (number) of your exercise programme and confirm by pressing ENTER:")
        continue
    else:
        day = int(day)
        break
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
    return("00:00")


def bbg():
    print("Up next...\n")
    time.sleep(2)
    for item in circuit1:
        print(item)
    time.sleep(2)
    print(countdown(10), "\nCircuit completed.\n")
    time.sleep(2)
    print("Rest")
    time.sleep(2)
    print(countdown(5), "\n")
    print("Up next...\n")
    time.sleep(2)
    for item in circuit2:
        print(item)
    time.sleep(2)
    print(countdown(10), "\nCircuit completed.\n")
    time.sleep(2)


def bbg_recovery():
    print("Up next...\n")
    time.sleep(2)
    for item in recovery:
        print(item)
    time.sleep(2)
    input("\nThe recovery workout is finished once all items have been completed.\nPress ENTER once you are done.\n")

print("\nToday's workout is:", df.loc[df_line, "Workout"], "\n")
time.sleep(2)
if rec == "yes":
    bbg()
    print("Rest")
    time.sleep(2)
    print(countdown(5), "\n")
    bbg()
    input("Finished. Well done!\nPress Enter to close.")
else:
    bbg_recovery()
    input("Finished. Well done!\nPress Enter to close.")
