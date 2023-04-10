from tkinter import Frame
from tkinter import Canvas
from tkinter import Scrollbar
from src.frames.frame_sup import FrameSup
from src.frames.frame_inf import FrameInf
from src.controllers.controllers import get_user_contacts

class ContactsPage(Frame):

    def __init__(self, master, layouts,  id_user, **kwargs):
        super().__init__(master, **kwargs)

        self.layouts = layouts
        self.id_user = id_user

        self.configure( bg="#2774A8",bd=0, highlightthickness=0)

        contacts = get_user_contacts(self.id_user)

        canvas = Canvas(self, bg="#2774A8", bd=0, highlightthickness=0)
        scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas, bg="#2774A8", bd=0, highlightthickness=0)

        self.scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )    

        canvas.create_window((25, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        frame_sup= FrameSup(self.scrollable_frame, self.master, self.id_user, self.layouts, contacts)
        frame_sup.pack(fill="both", side="top", expand=1)

        frame_inf = FrameInf(self.scrollable_frame, 
                            self.master, 
                            self.id_user, 
                            self.layouts,
                            contacts)
        frame_inf.pack(fill="both", side="bottom", expand=1)

        canvas.pack()
        canvas.pack(fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")