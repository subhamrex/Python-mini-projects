# Imports
import time
from tkinter import *
import cv2
from PIL import Image, ImageTk
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import QUrl


class App:
    def __init__(self, video_source=0):
        self.player = QMediaPlayer()  # Initialize player for click sound
        self.app_name = "Camera"
        self.window = Tk()
        self.window.title(self.app_name)
        self.window.resizable(0, 0)
        self.window.wm_iconbitmap("camera.ico")
        self.window["bg"] = "#FBC088"
        self.video_source = video_source
        self.photo = None

        self.vid = MyVideoCapture(self.video_source)
        self.label = Label(self.window, text=self.app_name, font=20, bg="gray", fg="white").pack(side=TOP, fill=BOTH)

        # Create a canvas that can fit the above video source size
        self.canvas = Canvas(self.window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # Button which takes a snapshot
        self.btn_snapshot = Button(self.window, text="Snapshot", font="lucida 15 bold", width=30, bg="#8FB48E",
                                   activebackground="#564BF7",
                                   command=self.snapshot)
        self.btn_snapshot.pack(anchor=CENTER, expand=True)
        self.update()
        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        check, frame = self.vid.getFrame()
        if check:
            image = "IMG-" + time.strftime("%H-%M-%S-%d-%m") + ".jpg"
            cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Show the message on window that image was saved
            msg = Label(self.window, text="Image Saved: " + image, font="lucida 10 bold", bg="#EBC16A", fg="#36454F")
            msg.place(x=400, y=510)
            # Sound
            file = QUrl("click.wav")
            content = QMediaContent(file)
            self.player.setMedia(content)
            self.player.play()

    def update(self):
        # Get a frame from the video source
        isTrue, frame = self.vid.getFrame()
        if isTrue:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.window.after(15, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open Camera")

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def getFrame(self):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue:
                # If isTrue is true then current frame converted to RGB
                return isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return isTrue, None

    def __del__(self):
        self.vid.release()


if __name__ == "__main__":
    App()
