from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Checkbutton")
janela.geometry("200x200")

def teste():
    print(f"valor do checkbutton: {estado.get()}")

estado = IntVar()

chek = Checkbutton(janela, text="escolha", var=estado, onvalue=1, offvalue=0, command=teste)# o var recebe uma variavel, onde se tiver ativa recebe o valor da onvalue e se tiver desativada recebe o valor da offvalue
chek.grid(row=0, column=0)


janela.mainloop()