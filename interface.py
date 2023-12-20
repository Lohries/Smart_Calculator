from tkinter import *


def click():
    pass

def add():
    pass

def sub():
    pass

def multi():
    pass

def div():
    pass

def physics():
    pass

def volume():
    pass

def area():
    pass
 
    


#Creating window
window = Tk()
window.geometry("720x1280")
window.title("Calculator")

button = Button(window,     #Botton config
                text="Clique para começar",
                command=click,
                font=('Arial', 15),
                )
button.pack()

window.mainloop()