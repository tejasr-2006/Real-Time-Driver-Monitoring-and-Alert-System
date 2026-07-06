from ultralytics import YOLO

# Load model once
model = YOLO("yolov8n.pt")

# ---------- SETTINGS ----------
PHONE_CONF = 0.25
PERSON_CONF = 0.5

MIN_PHONE_AREA = 500
MIN_PERSON_AREA = 5000

PHONE_HOLD_FRAMES = 18

# ---------- MEMORY ----------
last_phone = None
phone_timer = 0


def detect_objects(frame):
    global last_phone, phone_timer

    results = model(frame)

    best_person = None
    best_phone = None

    for r in results:
        for box in r.boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            width = x2 - x1
            height = y2 - y1
            area = width * height

            # ---------- PERSON (keep largest) ----------
            if cls == 0:
                if conf < PERSON_CONF or area < MIN_PERSON_AREA:
                    continue

                if best_person is None or area > best_person["area"]:
                    best_person = {
                        "box": (x1, y1, x2, y2),
                        "area": area
                    }

            # ---------- PHONE (more tolerant) ----------
            elif cls == 67:
                if conf < PHONE_CONF or area < MIN_PHONE_AREA:
                    continue

                if best_phone is None or conf > best_phone["conf"]:
                    best_phone = {
                        "box": (x1, y1, x2, y2),
                        "conf": conf
                    }

    # ---------- PHONE MEMORY (ANTI-FLICKER) ----------
    if best_phone:
        last_phone = best_phone
        phone_timer = PHONE_HOLD_FRAMES
    else:
        if phone_timer > 0:
            phone_timer -= 1
            best_phone = last_phone
        else:
            last_phone = None

    # ---------- FINAL OUTPUT ----------
    persons = []
    phones = []

    if best_person:
        persons.append(best_person["box"])

    if best_phone:
        phones.append(best_phone["box"])

    return {
        "persons": persons,
        "phones": phones
    }



'''from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# ---- SETTINGS ----
PERSON_CONF = 0.5
PHONE_CONF = 0.3          # Lowered: better detection near ear
MIN_PHONE_AREA = 800

# ---- MEMORY (anti-flicker) ----
PHONE_HOLD_FRAMES = 12    # Increased: longer hold when phone moves
last_phone = None
phone_timer = 0


def detect(frame):
    global last_phone, phone_timer

    results = model(frame)

    best_person = None
    best_phone = None
    best_headphone = None

    for r in results:
        for box in r.boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # person (0), phone (67), headphones (73)
            if cls not in [0, 67, 73]:
                continue

            width = x2 - x1
            height = y2 - y1
            area = width * height

            # -------- PERSON (largest = driver) --------
            if cls == 0:
                if conf < PERSON_CONF:
                    continue

                if best_person is None or area > best_person["area"]:
                    best_person = {
                        "box": [x1, y1, x2, y2],
                        "area": area
                    }

            # -------- PHONE --------
            elif cls == 67:
                if conf < PHONE_CONF or area < MIN_PHONE_AREA:
                    continue

                if best_phone is None or conf > best_phone["conf"]:
                    best_phone = {
                        "box": [x1, y1, x2, y2],
                        "conf": conf
                    }

            # -------- HEADPHONES / EARPODS --------
            elif cls == 73:
                if conf < 0.3:
                    continue

                if best_headphone is None or conf > best_headphone["conf"]:
                    best_headphone = {
                        "box": [x1, y1, x2, y2],
                        "conf": conf
                    }

    # -------- PHONE MEMORY (ANTI-FLICKER) --------
    if best_phone:
        last_phone = best_phone
        phone_timer = PHONE_HOLD_FRAMES
    else:
        if phone_timer > 0:
            phone_timer -= 1
            best_phone = last_phone
        else:
            last_phone = None

    # -------- CLEAN OUTPUT --------
    output = {
        "persons": [],
        "phones": [],
        "earpods": []
    }

    if best_person:
        output["persons"].append(best_person["box"])

    if best_phone:
        output["phones"].append(best_phone["box"])

    if best_headphone:
        output["earpods"].append(best_headphone["box"])

    return output


# Wrapper (important for main.py)
def detect_objects(frame):
    return detect(frame)'''


