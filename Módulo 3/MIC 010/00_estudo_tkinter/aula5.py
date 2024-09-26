from tkinter import *

janela = Tk()

janela.title('Entry')
janela.geometry("300x300")

label = Label(janela, text="Entry") 
label.grid(row=0, column=0) 
entrada = Entry(janela, width=10) #adiciona o entrada de dados
entrada.grid(row=0, column=1) 

janela.mainloop()