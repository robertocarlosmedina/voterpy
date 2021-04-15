import sys
import os
from threading import Thread
# Thread apps that will allow multiple apps to be executed
class Threads(Thread):
    def __init__(self, app):
        Thread.__init__(self)
        self.app = app
    def run(self):
        print(self.app)
        # Starting the thread according to the app name sent
        os.system(f"python3 {self.app}/main.py")
        try:
            os.system(f"python3 {self.app}/main.py")
        except:
            pass

# Starting all the app that the user wants by threads
for i in range(1, len(sys.argv)):
    # send the files name written in the terminal when executing the code
    th = Threads(sys.argv[i]) 
    th.start()
