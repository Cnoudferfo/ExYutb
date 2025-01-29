# This doesn't work on Raspbian
# import keyboard  # using module keyboard

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        # if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        #     print('You Pressed A Key!')
        #     break  # finishing the loop
        the_ky = input('Enter a key: ')
        if the_ky == 'e':
            print('Exit this loop!')
            break  # finishing the loop
        elif the_ky == 'p':
            print('Pause the player!')
        elif the_ky == 'r':
            print('Resume the player!')
    except:
        print('Exception! break the loop!')
        break  # if user pressed a key other than the given key the loop will break