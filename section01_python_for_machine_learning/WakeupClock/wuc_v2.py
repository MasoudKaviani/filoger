import time
import winsound

def start_beep(secs):
    for i in range(int(secs)):
        winsound.Beep(2500, (i+1)*1000)

def counter(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        if len(str(secs)) == 1:
            secs = '0' + str(secs)
        timer = str(mins) + ':' + str(secs)
        print(timer, end='\r')
        time.sleep(1)
        t = t-1

t = int(input('Please Enter the Time in Seconds: '))
counter(t)
start_beep(3)
print('WakeUp')