from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Listbox")
janela.geometry("250x200")

listbox = Listbox(janela, height=8)
listbox.grid(row=0, column=0)

listbox.insert(0, "PHP") #<index>, <item>
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(END, "JavaScript") # insere no final da lista

janela.mainloop()