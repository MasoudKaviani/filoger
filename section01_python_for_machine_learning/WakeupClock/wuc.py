import time
import winsound

t = int(input('Please Enter the Time in Seconds: '))
print(t)
time.sleep(t)
for i in range(3):
    winsound.Beep(2500, (i+1)*1000)
print('goodbye')