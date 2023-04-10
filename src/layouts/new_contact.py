from tkinter import Frame
from tkinter import Label
from src.components.my_button import MyButton
from src.components.entry_label import LabelEntry
from utils.validators.validators import email_patron
from src.controllers.controllers import create_contact
from utils.helpers.helpers import message_change
class NewContact(Frame):

    def __init__(self, master, id_user, layouts, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(bg="#2774A8")
    
        self.id_user = id_user
        self.layouts = layouts

        bton_contacs = MyButton(self,"Return", command= self.click_contacts)
        bton_contacs.place(x=25, y=0) 

        self.name = LabelEntry(self, "Name :", 14, "Arial", bg="#2774A8")
        self.name.place(x=85, y=85)

        self.lastname = LabelEntry(self, "Last Name :", 14, "Arial", bg="#2774A8")
        self.lastname.place(x=45, y=130)

        self.email = LabelEntry(self, "Email :", 14, "Arial", bg="#2774A8")
        self.email.place(x=90, y=175)

        self.phone = LabelEntry(self,"Phone :", 14, "Arial", bg="#2774A8")
        self.phone.place(x= 82, y= 223 )

        self.message = Label(self, fg="#9C0015", font=("Arial",14), bg="#2774A8")
        self.message.place(x=175, y=285)

        bton_save = MyButton(self,"Save", command=self.click_save)
        bton_save.place(x=182, y=330)


    def click_contacts(self):
        for child in self.master.winfo_children():
            child.destroy()

        contacts_page = self.layouts["contacts_page"](self.master, self.layouts, self.id_user)
        contacts_page.pack(fill="both", expand=1)

    def click_save(self):
        if (self.name.get_entry() != "" and self.lastname.get_entry() != "" 
            and email_patron(self.email.get_entry()) != None and self.phone.get_entry() != ""):
            create_contact(self.id_user, 
                           self.name.get_entry(), 
                           self.lastname.get_entry(), 
                           self.email.get_entry(), 
                           self.phone.get_entry())

            for child in self.master.winfo_children():
                child.destroy()

            contacts_page = self.layouts["contacts_page"](self.master, self.layouts, self.id_user)
            contacts_page.pack(fill="both", expand=1)

        else:

            message_change(self.message, "Invalid data!")