try:
    with open('sweetnewfile.txt', mode= 'a') as file:
        file.writelines(['This is a new file', '\nThis is another line to be added'])
except FileNotFoundError as e:
    print('ERROR', e)
    '''
    with open('sweetnewfile.txt', mode= 'w') as file:
        file.writelines(['This is a new file', '\nThis is another line to be added'])
    '''
    #The commented out lines of code shows how to create a new file in python