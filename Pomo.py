#File to implement personal pomodoro technique

'''
Algorithm
#Take in 'start' keyword
#Start time
#Wait for stop keyword
#Calculate time
#Ask for category
#Ask for what work was done
#Save it to csv file
'''

from datetime import datetime as d

#startprint(d.now())
print("Enter 'start' when you are ready!!")
n = input()
if n == 'start':
    start = d.now()
print("Stop wasting time now!\nHead to work.\n\nType 'stop' when you are done with your session.")
n = input()

stop = d.now()
hours = stop.hour - start.hour
minutes = stop.minute - start.minute
duration = str(stop - start)
#duration = str(hours)+' hrs '+str(minutes)+' minutes '
print("Enter category:")
category = input()
print('Enter the activity:')
activity = input()

with open('Progress.csv',"a") as file:
    record = str(start)+','+str(stop)+','+duration+','+category+','+activity+'\n'
    file.write(record)