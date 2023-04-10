from tkinter import Tk
from src.layouts.conteiner import Conteiner
from src.layouts.login import Login
from src.layouts.register import Register
from src.layouts.contacts_page import ContactsPage
from src.layouts.new_contact import NewContact
from src.layouts.edit_contact import EditContact

layouts = {
    "contacts_page": ContactsPage,
    "edit_contact": EditContact,
    "login": Login,
    "new_contact": NewContact,
    "register": Register
}

class App(Tk):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
           
        self.geometry("450x600")
        self.resizable(False, False)
        self.title("PhoneBook")

        conteiner = Conteiner(self, layouts)
        conteiner.pack(fill="both", expand=1)

        self.mainloop()
