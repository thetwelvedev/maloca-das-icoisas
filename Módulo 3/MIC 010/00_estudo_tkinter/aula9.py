from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Listbox")
janela.geometry("250x200")

listbox = Listbox(janela, height=8)
listbox.grid(row=0, column=0)

linguagens_programacao = ["Python", "Java", "C", "C++", "JavaScript", "Ruby", "Go", "Swift"]

for i in linguagens_programacao:
    listbox.insert(END, i)

janela.mainloop()