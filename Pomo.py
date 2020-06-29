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

print(start.hour - stop.hour)
print(start.minute - stop.minute)
print(start.second - stop.second)

