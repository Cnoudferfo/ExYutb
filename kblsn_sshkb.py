# A keyboard listener using sshkeyboard
# This is going to be run on Raspbian's SSH mode
from sshkeyboard import listen_keyboard, stop_listening # using module sshkeyboard
import time

def on_press(key, key_handler):
    print(f'{key} pressed')
    if key_handler(key) == False:
        print('Quit the player...')
        stop_listening()    # Stop listening

def on_press_wrapper(key_handler):
    return lambda key: on_press(key, key_handler)

def on_release(key):
    print(f'{key} released')
    if key == 'esc':
        print('Stop listening...')
        stop_listening()    # Stop listening

# Collect events until released
def key_listener_wrapper(key_handler):
    listen_keyboard(
        on_press=on_press_wrapper(key_handler), 
        on_release=on_release, 
        sequential = True)

# To handle the key event
# return False to stop the listener
def handler(key) -> bool:
    print(f'handler: {key} pressed')
    if key == 'q':
        # Stop listener
        print('Quit...')
        return False
    else:
        return True

# Collect events until released
key_listener_wrapper(handler)