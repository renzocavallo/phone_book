from tkinter import Frame
from tkinter import Label
from src.components.my_button import MyButton
from src.components.entry_label import LabelEntry
from bcrypt import hashpw, gensalt
from utils.validators.validators import email_patron, password_patron
from src.controllers.controllers import create_user
from utils.helpers.helpers import message_change

class Register(Frame):

    def __init__(self, master, layouts, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(bg="#2774A8")

        self.layouts = layouts       
        
        self.name = LabelEntry(self, "Name :", 14, "Arial", bg="#2774A8")
        self.name.place(x=85, y=85)

        self.lastname = LabelEntry(self,"Last Name :", 14, "Arial", bg="#2774A8")
        self.lastname.place(x=45, y=130)

        self.email = LabelEntry(self, "Email :", 14, "Arial", bg="#2774A8")
        self.email.place(x=90, y=175)

        self.password = LabelEntry(self, "Password :", 14, "Arial", bg="#2774A8", text_e="Min. six characters")
        self.password.place(x= 52, y= 223 )

        self.message = Label(self, fg="#9C0015", font=("Arial",14), bg="#2774A8")
        self.message.place(x=175, y=285)

        bton_save = MyButton(self, text="Save", command= self.click_save)
        bton_save.place(x=182, y=330)

        go_login = Label(self, text="Back to login", font=("Arial", 14), bg="#2774A8")
        go_login.configure( cursor="hand2")
        go_login.place(x=170, y=390)

        go_login.bind("<ButtonRelease-1>", lambda e: self.click_go_login())

    def get_message(self):
        self.message["text"] = ""
        return self.message["text"]

    def get_message_error(self):
        return self.message["text"]

    def click_save(self):
        if (self.name.get_entry() != "" and self.lastname.get_entry()  != "" 
            and email_patron(self.email.get_entry()) != None 
            and password_patron(self.password.get_entry()) != None):

            hashed_password = hashpw(self.password.get_entry().encode('utf-8'), gensalt(12))

            if not create_user(self.name.get_entry(), 
                               self.lastname.get_entry(), 
                               self.email.get_entry(), 
                               hashed_password):
                
                message_change(self.message, "Existing email")

            else:

                for child in self.master.winfo_children():
                    child.destroy()
            
                login = self.layouts["login"](self.master, self.layouts)
                login.pack(fill="both", expand=1)

        else:

            message_change(self.message, "Invalid data!")

    def click_go_login(self):
        for child in self.master.winfo_children():
            child.destroy()

        login = self.layouts["login"](self.master, self.layouts)
        login.pack(fill="both", expand=1)