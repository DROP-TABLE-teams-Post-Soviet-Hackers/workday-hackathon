from threading import Thread
from classifier import is_bad_posture
from time import sleep

cur_loop_thread = None
is_started = False

def classify_loop():
    while(is_started):
        if(is_bad_posture()):
            print("bad")
        else:
            print("good")
        sleep(1)


def start():
    global cur_loop_thread, is_started

    if(cur_loop_thread != None):
        cur_loop_thread.join(0)

    cur_loop_thread = Thread(target=classify_loop)
    cur_loop_thread.start()

    is_started = True

def stop():
    global is_started
    is_started = False


start()
sleep(5)
stop()
print("stopped")
sleep(10)
start()
sleep(10)
stop()
