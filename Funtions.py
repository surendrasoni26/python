def make_shirt(size, message):
    print('your shirt size is ' + size)
    print('Messgae will be printed on t-shirt is ' + message)

make_shirt('large', 'Be positive')

print('################')

def make_shirt(size, message):
    """function to check a default entry"""
#    print('your shirt size is ' + size)
#    print('Messgae will be printed on t-shirt is ' + message)
    if size == 'large':
        message = 'I love python'
        print ('Messgae will be printed on t-shirt is ' + message)
    else:
        print ('Messgae will be printed on t-shirt is ' + message)
"""1st Call"""
make_shirt('large', 'Be positive')
"""2nd Call"""
make_shirt('small', 'Stay Focused')

print('################')

def make_shirt(size, message='Aim High'):
    """default value function example"""
    print('your shirt size is ' + size)
    print('Messgae will be printed on t-shirt is ' + message)

make_shirt(size='large')
