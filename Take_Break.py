import webbrowser
import time

total_breaks = 3
break_count = 0

print 'This program started on ' +time.ctime()
while break_count < 3:
        time.sleep(7200)
        webbrowser.open('http://anayatchowdhury.co.uk')
        break_count = break_count + 1