from tkinter import Frame
from tkinter import Label
from src.components.my_button import MyButton
from src.components.entry_label import LabelEntry
from utils.helpers.helpers import message_change
from src.controllers.controllers import log_success

class Login(Frame):

    def __init__(self, master, layouts, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(bg="#2774A8") 
        self.succes = 0
        self.layouts = layouts

        self.l_e_email = LabelEntry(self, "Email :", 14, "Arial", bg="#2774A8")
        self.l_e_email.place(x=92, y= 170)

        self.l_e_pass = LabelEntry(self, "Password :", 14 , "Arial", "*", bg="#2774A8")
        self.l_e_pass.place(x= 55, y= 210)

        go_register = Label(self, text="Click here to register!")
        go_register.configure( bg="#2774A8", cursor="hand2", font=("Arial", 14))
        go_register.place(x=145, y=350)

        bton_login = MyButton(self, "Get into" ,command=self.click_get_into)
        bton_login.place(x= 190, y=290)
  
        self.message = Label(self, fg="#9C0015", font=("Arial", 14), bg="#2774A8")
        self.message.place(x=100, y=250) 

        go_register.bind("<ButtonRelease-1>", lambda e: self.check_in())

    def click_get_into(self):
        if self.l_e_email.get_entry() != "" and self.l_e_pass.get_entry() != "":
            self.succes = log_success(self.l_e_email.get_entry(), self.l_e_pass.get_entry())
            if self.succes != 0:
                for child in self.master.winfo_children():
                    child.destroy()
            
                contact_page = self.layouts["contacts_page"](self.master, self.layouts, self.succes)
                contact_page.pack(fill="both", expand=1)

            else:

                message_change(self.message, "Wrong username or password!")

    def check_in(self):
        for child in self.master.winfo_children():
            child.destroy()
        
        register = self.layouts["register"](self.master, self.layouts)
        register.pack(fill="both", expand=1)