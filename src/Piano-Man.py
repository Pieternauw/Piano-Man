import datetime
import os
import time 
import random 
import webbrowser
        
ninepm = "9:00"
try:
    nine = [int(n) for n in ninepm.split(":")]
except ValueError:
    print("Wrong format")


now = datetime.datetime.now()
seconds_hms = [3600, 60, 1] #seconds in hour, minute, second
now_sec = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

alarm_sec = sum([a*b for a,b in zip(seconds_hms[:len(nine)], nine)])

time_dif = alarm_sec - now_sec

if time_dif < 60:
    time_dif += 86400
    
if not os.path.isfile("explanation.html"):
    with open("explanation.html", "w") as expl:
        expl.write("<!DOCTYPE html><body><p>It's not quite time for piano man yet, check back in when the piano man is in session</p></body>")

if time_dif < 60 :
    webbrowser.open("https://youtu.be/gxEPV4kolz0")
else:
    webbrowser.open("explanation.html")
    