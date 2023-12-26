from tkinter import *

# Creating window
window = Tk()
window.geometry("920x580")
window.title("Advance Calculator")


def open_new_window(title):
    new_window = Toplevel(window)
    new_window.title(title)


def create_button(text, x, y, command):
    button = Button(window, text=text, font=('Arial', 15), command=command)
    button.place(x=x, y=y)


create_button("1", 150, 50, lambda: open_new_window("Soma"))
create_button("2", 250, 50, lambda: open_new_window("Subtracao"))
create_button("3", 350, 50, lambda: open_new_window("Multiplicar"))

create_button("4", 150, 150, lambda: open_new_window("Dividir"))
create_button("5", 250, 150, lambda: open_new_window("Areas Planas"))
create_button("6", 350, 150, lambda: open_new_window("Formulas Fisicas"))

create_button("7", 150, 250, lambda: open_new_window("Angulos"))
create_button("8", 250, 250, lambda: open_new_window("Areas Solidos"))
create_button("9", 350, 250, lambda: open_new_window("Volume"))

create_button("10", 150, 350, lambda: open_new_window("Derivadas"))
create_button("11", 250, 350, lambda: open_new_window("Integrais"))
create_button("12", 350, 350, lambda: open_new_window("Grafico"))

create_button("13", 250, 450, lambda: open_new_window("Sair"))

# New windows




window.mainloop()
