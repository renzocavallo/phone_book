from tkinter import Frame
from src.components.entry_label import LabelEntry
from src.components.my_button import MyButton
from src.components.card import Card
from src.controllers.controllers import search_contact

class FrameInf(Frame):

    def __init__(self, master, root, id_user, layouts, contacts, **kwargs):
        super().__init__(master, **kwargs)
  
        self.root = root
        self.layouts = layouts
        self. id_user = id_user

        self.configure(width=375, bg="#2774A8")

        self.l_e_search = LabelEntry(self, "Enter name :", 14, "Arial", bg="#2774A8")
        self.l_e_search.pack(side="top", pady=10, anchor="sw")

        bton_searh = MyButton(self, "Search", command= self.click_search)
        bton_searh.pack(side="top", pady=5)

        self.container_cards = Frame(self, bg="#2774A8")
        self.container_cards.pack(side="bottom", fill="both", expand=1)

        for contact in contacts:
              
            card = Card(self.container_cards, contact)
            card.pack(side="top", fill="both", pady=5)
             
            def make_lambda(contact):
                return lambda e: self.click_edit_contact(contact)
            
            card.bind("<ButtonRelease-1>", make_lambda(contact))

    def click_edit_contact(self, contact):
        for child in self.root.winfo_children():
            child.destroy()

        edit_contact = self.layouts["edit_contact"](self.root , contact,self.id_user, self.layouts)
        edit_contact.pack(fill="both", expand=1)

    def click_search(self):
        contacts = search_contact(self.id_user, self.l_e_search.get_entry())

        for child in self.container_cards.winfo_children():
            child.destroy()

        for contact in contacts:
              
            card = Card(self.container_cards, contact)
            card.pack(side="top", fill="both", pady=5)
             
            def make_lambda(contact):
                return lambda e: self.click_edit_contact(contact)
            
            card.bind("<ButtonRelease-1>", make_lambda(contact))
