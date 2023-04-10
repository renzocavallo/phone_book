from tkinter import Frame
from tkinter import Label
from tkinter import Entry

class LabelEntry(Frame):

    def __init__(self, master, text , font_s, font_f =None , show=None, bg=None, text_e=None, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(width= 300, height= 30, bg=bg)

        label = Label(self, text=text, font=(font_f, font_s ), bg=bg)
        label.pack(side="left", padx=3)
        self.entry = Entry(self, show=show ,highlightthickness= 0, bd=0, font=(font_f, font_s))

        if text_e != None:
            self.entry.insert(0, text_e)
            
        self.entry.pack(side="left", ipady=4)
    
    def get_entry(self):
        return self.entry.get()