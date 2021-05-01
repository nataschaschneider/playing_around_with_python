import time


def countdown(t):
    t = int(t)
    while t > -1:
        min, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, secs)
        print(timer,"seconds", end="\r")
        time.sleep(1)
        t -= 1
    return("00:00")


def abort():
    password = input("Enter password to abort. Confirm by pressing 'Enter':\n")
    while password != "Hallo!":
        password = input("Incorrect password. Please try again:\n")
    else:
        print("\nInitiation of brainwash.exe has been aborted.\n")
        time.sleep(2)
        print("The file world_domination.exe can no longer be executed.\n")
        time.sleep(2)
        print("Self-destruction of all microchips will be executed in:")
        countdown(10)
        time.sleep(2)

time.sleep(1)
print("Executing evil_masterplan.py.\n")
time.sleep(2)
print("Please wait for brainwash.exe and world_domination.exe to be downloaded.")
time.sleep(2)
loading = [2, 15, 23, 41, 78, 94, 98, 100, ""]
for i in loading:
    time.sleep(1)
    print(f"{i} %", end="\r")
print("Download complete.\n")
time.sleep(2)
print("Initiating brainwash.exe.\n")
time.sleep(1)
abort()
