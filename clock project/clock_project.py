import time
import os

hour = int(input("Enter Hour: => "))
minutes = int(input("Enter Minutes: => "))
seconds = int(input("Enter Seconds: => "))
if hour >= 24: hour = 0
if minutes >= 60: minutes = 0
if seconds >= 60: seconds = 0

while True:
    print( f"{hour}:{minutes}:{seconds}")
    seconds+=1
    if seconds >= 60:
        seconds = 0
        minutes += 1
    if minutes >= 60:
        minutes = 0
        hour += 1
    if hour >= 24:
        hour = minutes = seconds = 0
    time.sleep(1)
    os.system("cls")

