import os
import time
from Tkinter import *

from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.root = root
        self.imageLabel = None

        self.buttonFrame = None
        self.countdownLabel = None
        self.countdownText = StringVar()

        self.imageButton = None

        self.init_window()

    def init_window(self):
        self.root.title("PartyBooth")
        self.pack(fill=BOTH, expand=True)

        self.root.image = ImageTk.PhotoImage(file='resources/images/splash.png')
        background = Label(self.root, image=self.root.image)
        background.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.initButtons()
        self.showButtons()


    def initButtons(self):
        self.buttonFrame = Frame(self.root, width='700', height='740')

        self.imageButton = Label(self.buttonFrame, fg='white', bg='red', borderwidth=10,
                                 text="Tap to take photo!", font=("Sans", 80))
        self.imageButton.bind("<Button-1>", self.takePicture)
        self.imageButton.pack()
        # quitButton = Button(root, text="Quit", command=self.clientExit)
        # quitButton.place(x=0,y=0)

    def showButtons(self):
        self.buttonFrame.pack()

    def hideButtons(self):
        self.buttonFrame.destroy()

    def clientExit(self):
        exit()

    def showCountDown(self):
        self.countdownText.set("Tap to take photo!")

        self.countdownLabel = Label(self.master, fg='white', bg='red', borderwidth=10,
                                 textvariable=self.countdownText, font=("Sans", 80))

        self.countdownLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        countdown_length = 3
        for i in range(3):
            self.countdownText.set(str(countdown_length - i))
            self.countdownLabel.update()
            time.sleep(1)

        self.countdownText.set("Smile!")
        self.countdownLabel.update()
        time.sleep(1)

    def showImage(self):
        self.countdownText.set("Processing Image...")
        self.countdownLabel.update()
        load = Image.open(os.path.join("test", "images", "1.jpg"))
        print(load.format, load.size, load.mode)
        load = load.resize((700, 466), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image=load)
        self.imageLabel = Label(root, image=render, padx=0, pady=0, borderwidth=5, background='white')
        self.imageLabel.image = render
        self.imageLabel.bind("<Button-1>", self.hideImage)

        self.countdownLabel.destroy()
        self.imageLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.master.after(3000, self.hideImage, None)

    def takePicture(self, event):
        self.hideButtons()
        self.showCountDown()
        self.showImage()

    def hideImage(self, event):
        self.imageLabel.destroy()
        self.initButtons()
        self.showButtons()

root = Tk()
# root.geometry("800x480")
root.attributes("-fullscreen", True)
app = Window(root)
root.mainloop()
