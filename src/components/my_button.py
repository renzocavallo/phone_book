from tkinter import Button

class MyButton(Button):

    def __init__(self, master, text, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(relief="sunken", 
                        text=text,
                        font=("Arial", 12), 
                        cursor="hand2", 
                        width= 10 , 
                        height=2, 
                        bg="black" , 
                        foreground="white",
                        activeforeground="white" ,
                        activebackground="black" ,  
                        bd=0, 
                        highlightthickness=0)