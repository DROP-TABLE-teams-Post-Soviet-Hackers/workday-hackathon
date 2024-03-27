from threading import Thread
from classifier import is_bad_posture
from time import sleep

def start_classifiying():
    while(True):
        if(is_bad_posture()):
            print("bad")
        else:
            print("good")
        sleep(5)


thread = Thread(target=start_classifiying)
thread.start()