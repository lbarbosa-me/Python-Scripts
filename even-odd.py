#Even or odd
while True:
    try:
        value = int(input('Tap a number: '))
        if value % 2 == 0:
            print('Even')
        else:
            print('Odd')
    except:
        print('Please try again (Only numbers).')