"""This is a program which will act as a timer, or stopwatch
taking user input to determine how long the timer will be for
and then terminating once the specified time has elapsed."""

import time

def countdown(t):
    
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1
    
    print('Timer Up!!!')


t = input('Enter time in seconds: ')

countdown(int(t))