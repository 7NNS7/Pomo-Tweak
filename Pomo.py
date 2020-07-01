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
n = input()
if n == 'start':
    start = d.now().time()

n = input()
stop = d.now().time()

hours = start.hour - stop.hour
minutes = start.minute - stop.minute
duration = str(hours)+' hrs '+str(minute)+" minutes "
print("Enter category:")
category = input()
print('Enter the activity:')
activity = input()

with open('Progress.csv',"a") as file:
    record = start+','+stop+','+duration+','+category+','+activity+'\n'
    file.write(record)