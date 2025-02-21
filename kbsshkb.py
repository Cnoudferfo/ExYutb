# kbsshkb.py : A keyboard application class using sshkeyboard
# This is a wrapper for sshkeyboard.listen_keyboard and is going to be run on Raspbian's SSH mode
# By sending a higher level callback and create KbApp, this object will block
# The caller application need to handle all the events at the callback function
from sshkeyboard import listen_keyboard, stop_listening # using module sshkeyboard

class KbApp:
    def __init__(self, callback):
        # Collect events until released
        listen_keyboard(
            on_press = self.on_press_wrapperself(callback),
            on_release = self.on_release,
            sequential = True
        )

    def on_press(self, key, key_handler):
        if key_handler(key) == False:
            stop_listening()    # Stop listening

    def on_press_wrapperself(self, key_handler):
        return lambda key: self.on_press(key, key_handler)

    def on_release(self, key):
        if key == 'esc':
            print('Stop listening...')
            stop_listening()    # Stop listening

def a_sample_kb_handler(key) -> bool:
    print(f'handler: {key} pressed')
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