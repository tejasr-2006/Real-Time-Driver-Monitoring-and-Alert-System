import time

# -------------------------
# GLOBAL VARIABLES
# -------------------------
phone_start_time = None
total_phone_time = 0

phone_usage_count = 0
was_using_phone = False

focus_counter = 0
last_alert_time = 0

# NEW: fallback memory
last_phone_seen_time = 0
PHONE_MEMORY = 3

ALERT_COOLDOWN = 2


def decision_engine(data):
    global phone_start_time, total_phone_time
    global phone_usage_count, was_using_phone
    global focus_counter, last_alert_time
    global last_phone_seen_time

    phones = data.get("phones", [])
    earpods = data.get("earpods", [])
    head_direction = data.get("head_direction", "center")

    current_time = time.time()

    # DEFAULT ALERT
    alert = "safe"

    # -------------------------
    # PHONE DETECTED
    # -------------------------
    if len(phones) > 0:

        # remember last phone detection
        last_phone_seen_time = current_time

        # start timer
        if phone_start_time is None:
            phone_start_time = current_time

        # update usage time
        total_phone_time = int(current_time - phone_start_time)

        # usage count
        if not was_using_phone:
            phone_usage_count += 1
            was_using_phone = True

        # alert after delay
        if current_time - phone_start_time > 2.5:
            alert = "phone_alert"

    # -------------------------
    # PHONE FALLBACK
    # -------------------------
    elif current_time - last_phone_seen_time < PHONE_MEMORY:

        # continue alert temporarily
        alert = "phone_alert"

    # -------------------------
    # NO PHONE
    # -------------------------
    else:
        phone_start_time = None
        was_using_phone = False
        total_phone_time = 0

    # -------------------------
    # EARPOD ALERT
    # -------------------------
    if alert == "safe":
        if len(earpods) > 0:
            alert = "earpod_alert"

    # -------------------------
    # FOCUS ALERT
    # -------------------------
    if alert == "safe":

        if head_direction == "down":
            focus_counter += 1

            if focus_counter > 12:
                alert = "focus_alert"

        else:
            focus_counter = 0

    # -------------------------
    # FINAL OUTPUT
    # -------------------------
    return {
        "alert": alert,
        "time": total_phone_time,
        "count": phone_usage_count
    }

'''import time

# -------------------------
# GLOBAL VARIABLES
# -------------------------
phone_start_time = None
total_phone_time = 0

phone_usage_count = 0
was_using_phone = False

focus_counter = 0
last_alert_time = 0

ALERT_COOLDOWN = 2


def decision_engine(data):
    global phone_start_time, total_phone_time
    global phone_usage_count, was_using_phone
    global focus_counter, last_alert_time

    phones = data.get("phones", [])
    earpods = data.get("earpods", [])
    head_direction = data.get("head_direction", "center")

    current_time = time.time()

    alert = "safe"

    # -------------------------
    # PHONE LOGIC (PRIORITY)
    # -------------------------
    if len(phones) > 0:
        if phone_start_time is None:
            phone_start_time = current_time

        # Track time
        total_phone_time = int(current_time - phone_start_time)

        # Count usage (only when new usage starts)
        if not was_using_phone:
            phone_usage_count += 1
            was_using_phone = True

        # Alert after delay
        if current_time - phone_start_time > 2.5:
            if current_time - last_alert_time > ALERT_COOLDOWN:
                last_alert_time = current_time
            alert = "phone_alert"

    else:
        phone_start_time = None
        was_using_phone = False
        total_phone_time = 0

    # -------------------------
    # EARPOD LOGIC (HIGH PRIORITY AFTER PHONE)
    # -------------------------
    if len(earpods) > 0:
        alert = "earpod_alert"

    # -------------------------
    # FOCUS LOGIC (LOW PRIORITY)
    # -------------------------
    if alert == "safe":   # only trigger if no phone/earpod
        if head_direction == "down":
            focus_counter += 1

            if focus_counter > 12:
                if current_time - last_alert_time > ALERT_COOLDOWN:
                    last_alert_time = current_time
                alert = "focus_alert"
        else:
            focus_counter = 0

    # -------------------------
    # RETURN DATA (IMPORTANT CHANGE)
    # -------------------------
    return {
        "alert": alert,
        "time": total_phone_time,
        "count": phone_usage_count
    }'''