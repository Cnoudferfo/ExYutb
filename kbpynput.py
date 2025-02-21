# kbpynput.py : A keyboard application class using pynput
# This is a wrapper for sshkeyboard.listen_keyboard and is going to be run on Raspbian's SSH mode
# By sending a higher level callback and create KbApp, this object will block
# The caller application need to handle all the events at the callback function
from pynput import keyboard

class KbApp:
    def __init__(self, callback):
        # Collect events until released
        with keyboard.Listener(
                on_press=self.on_press_wrapper(callback),
                on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key, handler) -> bool:
        try: # To process alphanumeric keys only
            return handler(key.char)
        except AttributeError: # To process special keys only
            print(f'{key} pressed')
            return True
        
    def on_press_wrapper(self, key_handler):
        return lambda key: self.on_press(key, key_handler)

    def on_release(self, key) -> bool:
        if key == keyboard.Key.esc:
            # Stop listener
            print('Stop listening...')
            return False
        else:
            return True

def a_sample_kb_handler(key) -> bool:
    if key == 'q':
        # Stop listener
        print('Quit...')
        return False
    else:
        print(f'a_kb_handler: {key} pressed')
        return True

if __name__ == '__main__':    
    app = KbApp(a_sample_kb_handler)
    print(f'kbapp: {app} ended')