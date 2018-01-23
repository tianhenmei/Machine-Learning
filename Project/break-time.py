import webbrowser
import time
time_control = 0
time_total = 3
print('Current Time: '+time.ctime())
while(time_control < time_total):
    time.sleep(5)
    webbrowser.open("http://www.baidu.com")
    time_control += 1

