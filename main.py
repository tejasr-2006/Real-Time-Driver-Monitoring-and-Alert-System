import cv2
from detection import detect_objects
from focus import get_focus
from decision import decision_engine
from alert import show_alert

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # -----------------------
    # 1. Detection
    # -----------------------
    data = detect_objects(frame)

    # -----------------------
    # 2. Focus
    # -----------------------
    head_direction = get_focus(frame)
    data["head_direction"] = head_direction

    # -----------------------
    # 3. Decision
    # -----------------------
    result = decision_engine(data)

    alert = result["alert"]
    time_on_phone = result["time"]
    usage_count = result["count"]
    
    print(alert)

    # -----------------------
    # 4. Draw detection boxes
    # -----------------------
    for p in data.get("persons", []):
        x1, y1, x2, y2 = map(int, p)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    for ph in data.get("phones", []):
        x1, y1, x2, y2 = map(int, ph)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # -----------------------
    # 5. Show focus text
    # -----------------------
    cv2.putText(frame, f"Focus: {head_direction}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    # -----------------------
    # 6. Alert system
    # -----------------------
    show_alert(frame, alert, time_on_phone, usage_count)

    # -----------------------
    # 7. Display
    # -----------------------
    cv2.imshow("Driver Alert System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()