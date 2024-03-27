from threading import Thread
from classifier import is_bad_posture
from time import sleep

cur_loop_thread = None
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
    
    if(cur_loop_thread != None):
        cur_loop_thread.join()
        
    cur_loop_thread = Thread(target=classify_loop)
    cur_loop_thread.start()


def stop():
    global is_started
    is_started = False
