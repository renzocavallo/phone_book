from tkinter import Frame
from tkinter import Label
from src.components.my_button import MyButton
from src.controllers.controllers import get_user_email

class FrameSup(Frame):

    def __init__(self, master, root, id_user, layouts, contacts, **kwargs):
        super().__init__(master, **kwargs)

        self.root = root
        self.id_user = id_user 
        self.layouts = layouts

        self.configure(width=375 ,height=80, bg="#2774A8")
        
        data = get_user_email(self.id_user)

        email = Label(self, text= data, font=("Arial", 10), bg="#2774A8")
        email.place( x= 0, y= 42)

        count_contacts = Label(self, text= f"Contacts: {len(contacts)}", font=("Arial", 10), bg="#2774A8")
        count_contacts.place(x= 0, y= 62)

        bton_quit = MyButton(self, "Exit", command=self.master.quit)
        bton_quit.place(x= 0, y= 0)

        create_contact = Label(self, 
                            text="Add contact", 
                            bg="#2774A8", 
                            fg="black", 
                            cursor="hand2", 
                            font=("Arial", 14))
        create_contact.place(x= 265, y= 8)

        create_contact.bind("<ButtonRelease-1>", lambda e : self.click_new_contact())

    def click_new_contact(self):
        for child in self.root.winfo_children():
                child.destroy()

        new_contact = self.layouts["new_contact"](self.root, self.id_user, self.layouts)
        new_contact.pack(fill="both", expand=1)