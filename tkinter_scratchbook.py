import os
import time
from Tkinter import *

from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, root=None):
        Frame.__init__(self, root)

        self.root = root

        self.init_window()

    def init_window(self):
        self.root.title("PartyBooth")
        self.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.showButtons()

    #FIXME Memory Leak - show buttons defines new UI elements per call. Separate Setup from Display state management
    def showButtons(self):
        # quitButton = Button(root, text="Quit", command=self.clientExit)
        # quitButton.place(x=0,y=0)


        self.buttonFrame = Frame(root, width='700', height='740')
        self.buttonFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.imageButtonText = StringVar()
        self.imageButtonText.set("Tap to take photo!")
        self.imageButton = Label(self.buttonFrame, fg='white', bg='red', borderwidth=10,
                                 textvariable=self.imageButtonText, font=("Helvetica", 80))
        self.imageButton.bind("<Button-1>", self.showImage)
        self.imageButton.grid(sticky=N + S + E + W)


    def clientExit(self):
        exit()

    def showImage(self,event):
        countdown_length = 3
        for i in range(3):
            self.imageButtonText.set(str(countdown_length - i))
            self.imageButton.update()
            time.sleep(1)

        self.imageButtonText.set("Smile!")
        self.imageButton.update()
        time.sleep(1)

        load = Image.open(os.path.join("test","images","1.jpg"))
        print(load.format, load.size, load.mode)
        load = load.resize((700, 466), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image=load)
        imageLabel = Label(root,image=render,padx=0,pady=0,borderwidth=5,background='white')
        imageLabel.image = render
        imageLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        imageLabel.bind("<Button-1>", self.hideImage)
        self.buttonFrame.destroy()

    def hideImage(self, event):
        print('hideImage')
        self.showButtons()
        event.widget.destroy()

root = Tk()
# root.geometry("800x480")
root.attributes("-fullscreen", True)
root.image = ImageTk.PhotoImage(file='resources/images/splash.png')
background = Label(root, image = root.image)
background.place(relx=0.5, rely=0.5, anchor=CENTER)

app = Window(root)
root.mainloop()
