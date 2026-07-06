import cv2
import time
import threading
import winsound

last_alert_time = 0
last_alert_type = None
is_beeping = False

COOLDOWN = 2

def play_beep(frequency):
    global is_beeping
    is_beeping = True
    winsound.Beep(frequency, 500)
    is_beeping = False


def show_alert(frame, alert, time_on_phone, usage_count):
    global last_alert_time, last_alert_type, is_beeping

    current_time = time.time()

    # -------------------------
    # ALERT TYPE
    # -------------------------
    if alert == "phone_alert":
        text = "PHONE USAGE DETECTED!"
        freq = 1200

    elif alert == "focus_alert":
        text = "FOCUS ON ROAD!"
        freq = 900

    elif alert == "earpod_alert":
        text = "EARPOD USAGE DETECTED!"
        freq = 1000

    else:
        return

    # -------------------------
    # BACKGROUND BOX
    # -------------------------
    cv2.rectangle(frame, (40, 40), (650, 180), (0, 0, 0), -1)

    # -------------------------
    # MAIN ALERT TEXT
    # -------------------------
    cv2.putText(frame, text, (50, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # -------------------------
    # EXTRA INFO (NEW FEATURE)
    # -------------------------
    cv2.putText(frame, f"Time on Phone: {time_on_phone}s", (50, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.putText(frame, f"Usage Count: {usage_count}", (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # -------------------------
    # SOUND CONTROL
    # -------------------------
    if (current_time - last_alert_time > COOLDOWN or alert != last_alert_type) and not is_beeping:
        threading.Thread(target=play_beep, args=(freq,), daemon=True).start()
        last_alert_time = current_time
        last_alert_type = alert