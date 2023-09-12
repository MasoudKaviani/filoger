import random
import string
c = input('Please enter number of chars: ')
t = string.ascii_letters + string.digits
password = ''.join(random.sample(t+t+t, int(c)))
print(password)