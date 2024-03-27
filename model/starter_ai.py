from threading import Thread
from classifier import is_bad_posture
from time import sleep
from classifier import posture_checker
cur_loop_thread = None
is_started = False


def classify_loop():
    try:
        while (is_started):
            class_name = posture_checker()
            print(class_name)

    except Exception as e:
        print("Error in classifying loop:", e)


def start():
    global cur_loop_thread, is_started

    is_started = True

    if (cur_loop_thread != None):
        cur_loop_thread.join()

    cur_loop_thread = Thread(target=classify_loop)
    cur_loop_thread.start()


def stop():
    global is_started
    is_started = False


