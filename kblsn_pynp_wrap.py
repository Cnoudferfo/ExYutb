# Description: This is a wrapper for pynput.keyboard.Listener
#    To send a higher level callback to the listener
# This is NOT supported by Raspberry
from pynput import keyboard

def on_press(key, key_handler) -> bool:
    try:
        # To process alphanumeric keys only
        return handler(key.char)
    except AttributeError:
        # To process special keys only
        print(f'{key} pressed')
        return True
    
def on_press_wrapper(key_handler):
    return lambda key: on_press(key, key_handler)

def on_release(key) -> bool:
    if key == keyboard.Key.esc:
        # Stop listener
        print('Stop listening...')
        return False
    else:
        # print(f'{key} release')
        return True

# Collect events until released
def key_listener_wrapper(key_handler):
    with keyboard.Listener(
            on_press=on_press_wrapper(key_handler),
            on_release=on_release) as listener:
        listener.join()

# To handle the alphanumeric key event
# Return False to stop the listener
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
