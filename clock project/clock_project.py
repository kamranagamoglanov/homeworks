import datetime
import time
import os


hours_input = int(input("Enter Hour: => "))
minutes_input = int(input("Enter Minutes: => "))
seconds_input = int(input("Enter Seconds: => "))

def second():
    x = datetime.datetime(2024, 3, 2, 10, 20, seconds_input)
    return x.strftime("%S")
    
def minute():
    x = datetime.datetime(2024, 3, 2, 10, minutes_input, 0)
    return x.strftime("%M")
    
def hour():
    x = datetime.datetime(2024, 3, 2, hours_input, 0, 0)
    return x.strftime("%H")

while True:
    def hour_minute_second():
        hours_ = hour()
        minutes_ = minute()
        seconds_ = second()
        hours = int(hours_)
        minutes = int(minutes_)
        seconds = int(seconds_)
        while True:
            print( f"{hours}:{minutes}:{seconds}")
            seconds+=1
            if seconds == 60:
                seconds = 0
                minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
            if hours == 24:
                hours = 0
                minutes = 0
                seconds = 0
            time.sleep(1)
            os.system("cls")
    hour_minute_second()
