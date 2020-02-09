

import time
from turtle import *
class Clock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.AlarmHour = 0
        self.AlarmMinute = 0

    def setTime(self):
        self.seconds = 0
        self.hours = eval(input("Set time in hour: "))
        self.minutes = eval(input("Set time in minutes: "))
        if self.hours > 23:
            print ("Error Enter time in 24HR FORMAT")
            self.hours = eval(input("Set time in hour: "))
        if self.minutes > 60:
            print("Error Enter time in 24HR FORMAT")
            self.minutes = eval(input("\nSet time in minutes: "))
        setup()
        t1 = Turtle()
        while True:
            t1.clear()
            t1.write(str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + ":" + str(self.seconds).zfill(2), font=("arial",25,"normal"))
            self.seconds +=1
            time.sleep(1)
            if self.AlarmHour == self.hours and self.AlarmMinute == self.minutes:
                print("\nIts Tiiiimmeeee!!!!")
            if (self.seconds == 60):
                self.minutes += 1
                self.seconds = 0
            if (self.minutes == 60):
                self.hours += 1
                self.minutes = 0
            if (self.hours == 24):
                self.hours = 0


    def setAlarm(self):
        self.AlarmHour = eval(input("Set Alarm time in hour: "))
        self.AlarmMinute = eval(input("Set Alarm time in minutes: "))
        if self.AlarmHour > 23:
            print ("Error Enter time in 24HR FORMAT")
            self.AlarmHour = eval(input("Set Alarm time in hour: "))
        if self.AlarmMinute > 60:
            print("Error Enter time in 24HR FORMAT")
            self.AlarmMinute = eval(input("Set Alarm time in minutes: "))

clock = Clock()
clock.setAlarm()
clock.setTime()

    
