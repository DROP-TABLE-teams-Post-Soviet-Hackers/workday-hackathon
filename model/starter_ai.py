from threading import Thread
from classifier import is_bad_posture
from time import sleep
from test2 import posture_checker

cur_loop_thread : Thread = None
is_started = False

def classify_loop():
    try:
        while(is_started):
            if(is_bad_posture()):
                print("bad")
            else:
                print("good")
            sleep(1)
    except Exception as e:
        print("Error in classifying loop:", e) 


def start():
    global cur_loop_thread, is_started

    is_started = True

    if cur_loop_thread != None:
        return
        
    cur_loop_thread = Thread(target=posture_checker)
    cur_loop_thread.start()

    cur_loop_thread.join()

def stop():
    global cur_loop_thread
    cur_loop_thread = None
