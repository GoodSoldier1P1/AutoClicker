import time
import threading
from pynput.mouse import Button, Controller

#pynput.keyboard uses keyboard events to start/stop clicker
from pynput.keyboard import Listener, KeyCode

#delay - delay between each click
#button - used to click in whatever direction you want to. .left|.middle|.right
#start_stop_key - key used to start/stop. should be from a key class or set using Keycode
#exit_key - used to terminate clicker. should be from key class or set using Keycode

delay = 0.001
button = Button.right
start_stop_key = KeyCode(char='z')
stop_key = KeyCode(char='x')

#threading is used to control clicks
class ClickMouse(threading.Thread):

    #delay and button are passed to check execution of clicker
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    #method to check and run loop until it is true
    #another loop if check if it is set to true or not
    #for mouse click set it to button and delay
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    #start_stop_key will stop clicking if running flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    
    #call exit method and when key is pressed it ternminates clicker
    elif key == stop_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()