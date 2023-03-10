import time  
import threading  
from pynput.keyboard import Key, Controller  
from pynput.keyboard import Listener, KeyCode  
from pynput import keyboard

keyboard = Controller()

TOGGLE_KEY = KeyCode(char="t")
typing = False

def typer():
    while True:
        if typing:
            keyboard.type('Hello World')
            keyboard.press(Key.enter)
        time.sleep(60)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global typing
        typing = not typing

type_thread = threading.Thread(target=typer)
type_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()