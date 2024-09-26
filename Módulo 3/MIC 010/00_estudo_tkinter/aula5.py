from tkinter import *

janela = Tk()

janela.title('Entry')
janela.geometry("300x300")

label_nome = Label(janela, text="Nome: ") 
label_nome.grid(row=0, column=0) 
nome = Entry(janela, width=20) #adiciona o entrada de dados
nome.grid(row=0, column=1) 

label_idade = Label(janela, text="Idade: ") 
label_idade.grid(row=1, column=0) 
idade = Entry(janela, width=20) #adiciona o entrada de dados
idade.grid(row=1, column=1) 

label_pais = Label(janela, text="País: ") 
label_pais.grid(row=2, column=0) 
pais = Entry(janela, width=20) #adiciona o entrada de dados
pais.grid(row=2, column=1) 

def ler_entrada():
    n = nome.get() #get serve para ler os dados da Entry
    i = idade.get()
    p = pais.get()

    print(n, i, p)

btn = Button(janela, text="Clique", bg="blue", command=ler_entrada)
btn.grid(row=3, column=0)

janela.mainloop()