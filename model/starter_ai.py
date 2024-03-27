import datetime
import json
import sys
from threading import Thread
from time import sleep

import notifypy
from classifier import is_bad_posture, posture_checker
from loader import *
from PyQt5.QtWidgets import *
from sound import *

cur_loop_thread = None
is_started = False


def notif_with_notifpy(title: str, message: str):
    """
    Sends a notification using the notif-py engine.

    Args:
        title: str: the title of the notification
        message: str: the message of the notification
    Note:
        Cross-Platform: could be used on any OS.
    """
    notification = notifypy.Notify(enable_logging=True)  # I like enabling logging :)
    notification.application_name = "Hello, your posture is bad now!"
    notification.title = title
    notification.message = message
    notification.urgency = "critical"

    notification.send(
        block=False
    )  # block=False spawns a separate thread inorder not to block the main app thread


def classify_loop():
    global is_bended, last_time_notification
    try:
        while is_started:
            if is_bad_posture():
                cur_date = datetime.datetime.now()
                if cur_date - last_time_notification > datetime.timedelta(seconds=8):
                    last_time_notification = cur_date
                    is_bended = True
                    notif_with_notifpy(
                        title="Hello, your posture is bad now!",
                        message="Improve it",
                    )
            else:
                print("good")
                if is_bended:
                    is_bended = False
                with open("../config.json", "r") as f:
                    data = json.load(f)
                sleep(data["frequency"] / 1000)

    except Exception as e:
        print("Error in classifying loop:", e)


def start():
    global cur_loop_thread, is_started

    is_started = True

    if cur_loop_thread != None:

        cur_loop_thread.join()

    cur_loop_thread = Thread(target=classify_loop)
    cur_loop_thread.start()


def stop():
    global is_started
    is_started = False
