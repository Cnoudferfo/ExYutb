# This is NOT supported by Raspberry
from pynput import keyboard

def on_press(key) -> bool:
    try:
        print(f'{key} pressed')
        if key.char == 'q':
            # Stop listener
            print('Quit...')
            return False
        else:
            return True
    except AttributeError:
        print(f'{key} pressed')
        return True

def on_release(key) -> bool:
    if key == keyboard.Key.esc:
        # Stop listener
        print('Stop listening...')
        return False
    else:
        print(f'{key} release')
        return True

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()