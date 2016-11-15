# import tkinter as tk   # python3
import Tkinter as tk   # python

from PIL import Image, ImageTk

from lib.pages.CountDownPage import CountDownPage
from lib.pages.PhotoReviewPage import PhotoReviewPage
from lib.pages.StartPage import StartPage

class PartyBooth(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("800x480")
        #self.attributes("-fullscreen", True)

        image = ImageTk.PhotoImage(file='resources/images/splash.png')
        background = tk.Label(self, image=image)
        background.image = image
        background.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others, or grid.remove()d
        self.container = tk.Frame(self)
        #container.pack(side="top", fill="both", expand=True)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        #container.grid_propagate(0)

        self.frames = {}
        for F in (StartPage, CountDownPage, PhotoReviewPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        #background.lower()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        # only raise frame in question leaving the rest untouched
        #frame = self.frames[page_name]
        #frame.tkraise()

        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()
        self.update()
        frame.event_generate("<<FRAME_ACTIVATED>>")
        return frame


    def startCountDown(self):
        page = self.show_frame(CountDownPage.__name__)
        #page.countDown()

if __name__ == "__main__":
    app = PartyBooth()
    app.mainloop()