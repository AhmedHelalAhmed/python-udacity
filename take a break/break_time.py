import webbrowser
import time
total_breaks=3
break_count=1
while break_count<=total_breaks:
    time.sleep(2*60*60)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    break_count+=1

#https://www.youtube.com/watch?v=g3VbTGxk4Sg
#https://docs.python.org/2/library/webbrowser.html
#https://stackoverflow.com/questions/15472707/make-python-program-wait
#http://www.tutorialspoint.com/python/time_sleep.htm
#https://docs.python.org/2.7/library/index.html