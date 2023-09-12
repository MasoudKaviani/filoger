x2 = int(input('Please enter a number: '))
password = input('Please enter the password: ')
if password == 'jgsh78uhb' and not (x2 > 18):
    print('OK, you passed')
elif password == 'jgsh78uhb' and x2 > 14:
    print('OK, you passed napeloni')
else:
    print('NO, you have not passed the exam')