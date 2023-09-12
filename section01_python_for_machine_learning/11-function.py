def say_hello(first_name, last_name):
    print('hello', first_name)
    print('goodbye', last_name)


i = 10
j = 20
say_hello('Masoud', 'Kaviani')

print('last line')

def get_age(name, family='kaviani'):
    if name == 'Masoud':
        return 31
    elif name == 'Tavakoli':
        return 28
    else:
        return -1


age = get_age('Ali')
print(age)