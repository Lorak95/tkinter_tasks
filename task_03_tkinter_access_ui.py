from tkinter import *

ROOT = Tk()
ROOT.geometry("500x300+500+150")
ROOT.config(bg="grey")
ROOT.title("Ventana de acceso")

user_tag = Label(text="Usuario: ")
user_tag.grid(row=0, column=0)
user_tag.config(bg="grey", font=("Arial", 16))

password_tag = Label(text="Contraseña: ")
password_tag.grid(row=1, column=0)
password_tag.config(bg="grey", font=("Arial", 16))

user_input = Entry()
user_input.grid(row=0, column=1)
user_input.config(bg="red", font=("Comic Sans", 16))
user_input.insert(0, "Introduce tu usuario...") # Olvidé poner el argumento de posición

password_input = Entry()
password_input.grid(row=1, column=1)
password_input.config(bg="red", font=("Comic Sans", 16), show="*")
password_input.insert(0, "***********")

space_0 = Label(text=" ")
space_0.grid(row=3)
space_0.config(bg="grey")

space_1 = Label(text=" ")
space_1.grid(row=4, column=0)
space_1.config(bg="grey")

space_2 = Label(text=" ")
space_2.grid(row=2, column=0)
space_2.config(bg="grey")

def click_check_button():
    if password_input.get() == "python" and user_input.get() == "kenobi": # Olvidé añadir ".get()"
        access_granted = Label(text="¡Acceso concedido!")
        access_granted.grid(row=4, column=1)
        access_granted.config(bg="green", font=("Arial", 22))
        
    else:
        access_denied = Label(text="¡Acceso denegado!")
        access_denied.grid(row=4, column=1)
        access_denied.config(bg="red", font=("Arial", 22))


check_button = Button(text="Acceder", font=("Arial", 20))
check_button.grid(row=2, column=1)
check_button.config(bg="yellow", activebackground="orange", command=click_check_button)


ROOT.mainloop()