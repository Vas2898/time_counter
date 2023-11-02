import time

def count_down(time_sec):
    while time_sec:
        min, secs = divmod(time_sec, 60)
        timeformat = "{:02d}:{:02d}".format(min, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print('stop')
num = int(input("set timer : "))
count_down(num)
