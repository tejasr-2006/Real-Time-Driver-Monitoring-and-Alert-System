import tkinter as tk
from tkinter import Label, Button
import cv2
from PIL import Image, ImageTk

from detection import detect_objects
from focus import get_focus
from decision import decision_engine
from alert import show_alert

cap = cv2.VideoCapture(0)


class DriverGUI:

    def __init__(self, window):

        self.window = window
        self.window.title("Driver Alert Monitoring System")
        self.window.geometry("1100x750")
        self.window.configure(bg="black")

        # -------------------------
        # TITLE
        # -------------------------
        self.title = Label(
            window,
            text="AI DRIVER ALERT MONITORING SYSTEM",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="black"
        )
        self.title.pack(pady=10)

        # -------------------------
        # VIDEO FRAME
        # -------------------------
        self.video_label = Label(window)
        self.video_label.pack()

        # -------------------------
        # STATUS LABEL
        # -------------------------
        self.alert_label = Label(
            window,
            text="STATUS: SAFE",
            font=("Arial", 18, "bold"),
            fg="lime",
            bg="black"
        )
        self.alert_label.pack(pady=10)

        # -------------------------
        # PHONE TIME
        # -------------------------
        self.time_label = Label(
            window,
            text="Phone Usage Time: 0 sec",
            font=("Arial", 14),
            fg="white",
            bg="black"
        )
        self.time_label.pack()

        # -------------------------
        # USAGE COUNT
        # -------------------------
        self.count_label = Label(
            window,
            text="Usage Count: 0",
            font=("Arial", 14),
            fg="white",
            bg="black"
        )
        self.count_label.pack()

        # -------------------------
        # BUTTONS
        # -------------------------
        self.start_button = Button(
            window,
            text="START MONITORING",
            font=("Arial", 14, "bold"),
            bg="green",
            fg="white",
            command=self.update_frame
        )
        self.start_button.pack(pady=10)

        self.exit_button = Button(
            window,
            text="EXIT",
            font=("Arial", 14, "bold"),
            bg="red",
            fg="white",
            command=self.close
        )
        self.exit_button.pack(pady=10)

    def update_frame(self):

        ret, frame = cap.read()

        if ret:

            # -------------------------
            # DETECTION
            # -------------------------
            data = detect_objects(frame)

            # -------------------------
            # FOCUS
            # -------------------------
            head_direction = get_focus(frame)
            data["head_direction"] = head_direction

            # -------------------------
            # DECISION
            # -------------------------
            result = decision_engine(data)

            alert = result["alert"]
            time_on_phone = result["time"]
            usage_count = result["count"]

            # -------------------------
            # ALERT DISPLAY
            # -------------------------
            show_alert(frame, alert, time_on_phone, usage_count)

            # -------------------------
            # STATUS TEXT
            # -------------------------
            self.alert_label.config(text=f"STATUS: {alert.upper()}")

            self.time_label.config(
                text=f"Phone Usage Time: {time_on_phone} sec"
            )

            self.count_label.config(
                text=f"Usage Count: {usage_count}"
            )

            # -------------------------
            # CONVERT FRAME
            # -------------------------
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame_rgb)

            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        self.window.after(10, self.update_frame)

    def close(self):

        cap.release()
        self.window.destroy()


root = tk.Tk()

app = DriverGUI(root)

root.mainloop()