# This is a simple gui alarm clock program using tkinter.
# Note: not a reminder therefore you don't need to worry about dates.
# by Sandeep

import tkinter as tk
from datetime import datetime
import time

now = datetime.now()
print(now.strftime("%H:%M:%S"))

'''
hour = input("Enter the hour for which you wanna set time ")
minute = input("Enter the minute for which you wanna set time. ")

alarm_time = f"{hour}:{minute}"
print(alarm_time)
'''

# implementing the ui using tkinter.

# Variables for hours and minutes.
hour = list(range(1, 25))
minute = list(range(1, 60))

window = tk.Tk()
frame1 = tk.Frame(master=window)

h = tk.StringVar()
h.set("Hour")

m = tk.StringVar()
m.set("Minutes")

# hm = hour_menu, mm = minutes_menu (short names)
hm = tk.OptionMenu(frame1, h, *hour)
mm = tk.OptionMenu(frame1, m, *minute)

# This is done so that when value selected from dropddown, width dont'
# get changed.

hm.config(width=4)
mm.config(width=7)


frame1.pack()
hm.grid(row=0, column=0, padx=4, pady=2)
mm.grid(row=0, column =1, padx=4, pady=2)

# Creating function for setting time
def set(event):
    alarm_time = f"{h.get()}:{m.get()}"
    label["text"] = f"Ok! Alarm is set for {alarm_time}"

# Creating a button
button = tk.Button(master=window, text="Set", width=10)
button.pack(padx=5, pady=5)

#Creating a label
label = tk.Label(master=window, text="Set Timer")
label.pack()



def clock(event):
    # There is a problem happening, whenever while loop start running
    # label is now updating(label in set)
    alarm_time = f"{h.get()}:{m.get()}"
    label["text"] = f"Ok! Alarm is set for {alarm_time}"
    while True:
        now = datetime.now()
        time_now = now.strftime("%H:%M")
    
        if time_now == alarm_time:
            label["text"] = "Ringing..."
            break

        time.sleep(5)

button.bind("<Button-1>", set)

    

'''
while True:
    now = datetime.now()
    time_now = now.strftime("%H:%M")

    if alarm_time == time_now:
        print("Wake up!")
        break
    
    time.sleep(10)

    
 '''   
