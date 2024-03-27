from threading import Thread
from time import sleep

import notifypy
import plyer
from classifier import is_bad_posture, posture_checker

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


'''def notif_with_plyer(title: str, message: str):
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
    )'''


def classify_loop():
    try:
        while is_started:
            if is_bad_posture():
                """notif_with_plyer(
                    title="Hello, your posture is bad now!", message="Improve it"
                )"""
                notif_with_notifpy(
                    title="Hello, your posture is bad now!",
                    message="Improve it",
                )

            else:
                print("good")
            sleep(0.2)
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
