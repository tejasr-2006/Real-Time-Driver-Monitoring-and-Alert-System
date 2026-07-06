'''import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# -------- STABILITY VARIABLES --------
down_counter = 0
center_counter = 0
prev_focus = "center"

# Slightly increased for better stability
THRESHOLD = 6


def get_focus(frame):
    global down_counter, center_counter, prev_focus

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    # Default output
    focus = "center"

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]

        # Landmarks
        nose = face_landmarks.landmark[1]
        left_eye = face_landmarks.landmark[159]
        right_eye = face_landmarks.landmark[386]

        # Convert to pixel space
        nose_y = int(nose.y * h)
        eye_y = int(((left_eye.y + right_eye.y) / 2) * h)

        # -------- TUNED LOGIC --------
        # Slightly increased threshold to avoid false "down"
        if (nose_y - eye_y) > (0.06 * h):
            focus = "down"
        else:
            focus = "center"

    # -------- SMOOTHING --------
    if focus == "down":
        down_counter += 1
        center_counter = 0

        if down_counter >= THRESHOLD:
            prev_focus = "down"

    else:
        center_counter += 1
        down_counter = 0

        if center_counter >= THRESHOLD:
            prev_focus = "center"

    return prev_focus'''





import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Stability memory
focus_history = []
prev_focus = "center"

def get_focus(frame):
    global focus_history, prev_focus

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    focus = "center"  # default

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]

        # Nose tip
        nose = face_landmarks.landmark[1]

        # Eyes
        left_eye = face_landmarks.landmark[159]
        right_eye = face_landmarks.landmark[386]

        # Convert to pixel space
        nose_y = int(nose.y * h)
        eye_y = int(((left_eye.y + right_eye.y) / 2) * h)

        # Detection logic (tilted camera handled)
        if nose_y - eye_y > 40:
            focus = "down"
        else:
            focus = "center"

    else:
        focus = "no_face"

    # -------- STABILITY --------
    focus_history.append(focus)

    if len(focus_history) > 5:
        focus_history.pop(0)

    center_count = focus_history.count("center")
    down_count = focus_history.count("down")

    if down_count >= 4:
        prev_focus = "down"
    elif center_count >= 4:
        prev_focus = "center"

    return prev_focus