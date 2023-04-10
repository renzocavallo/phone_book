from tkinter import Frame

class Conteiner(Frame):

    def __init__(self, master, layouts, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(bg="#2774A8" ,bd=0, highlightthickness=0)

        login = layouts["login"](self, layouts )
        login.pack(fill="both", expand=1)