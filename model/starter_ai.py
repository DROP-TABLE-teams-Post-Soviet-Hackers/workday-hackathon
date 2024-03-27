from threading import Thread
from time import sleep
import json
import sys
import plyer
from classifier import is_bad_posture, posture_checker
from ui.NotificationDialog import NotificationDialog
from PyQt5.QtWidgets import *

cur_loop_thread = None
is_started = False


def notif_with_plyer(title: str, message: str):
    """
    Sends a notification using the plyer engine.

    Args:
        title: str: the title of the notification
        message: str: the message of the notification
    Note:
        Cross-Platform: could be used on any OS.
    """

    plyer.notification.notify(
        app_name="H4ck P0stur3",
        title=title,
        message=message,
        timeout=10,
    )


def classify_loop():
    try:
        while is_started:
            if is_bad_posture():
                with open("config.json", "r") as f:
                    data = json.load(f)
                if data["type"] == 1:
                    notif_with_plyer(
                        title="Hello, your posture is bad now!", message="Improve it"
                    )
                else:
                    app = QApplication(sys.argv)
                    form = NotificationDialog()
                    form.show()
                    app.exec_()
        else:
            print("good")
            with open("config.json", "r") as f:
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
