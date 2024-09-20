from tkinter import * # carrega todos os módulos da biblioteca
import random
#funções
def sair():
    janela.destroy()
def mudarCor():
    cores = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    cor_aleatoria = random.choice(cores)
    janela.configure(background=cor_aleatoria)
# Cria a janela principal
janela = Tk()
janela.configure(background='green')
janela.geometry('500x400')
janela.title("Controle de Relés via interface gráfica")
# Botão para fechar a janela
btn = Button(janela,text="Sair", command = sair)
btn.pack(padx=5, pady=5,side="bottom", expand=True, anchor="center")
# Botão para mudar a cor da janela
btn2 = Button(janela,text="Mudar de Cor", command = mudarCor)
btn2.pack(padx=5, pady=5,side="top", expand=True, anchor="center")

janela.mainloop()

"""
pack() Posicionamento sequencial
side:Especifica onde o botão será colocado dentro do contêiner (opções: top, bottom, left, right).
padx e pady: Adicionam preenchimento (espaço) ao redor do botão, em pixels, nas direções horizontal e vertical.
fill: Preenchimento dentro do espaço disponível
expand: Expansão para ocupar espaço disponível
expand=True: Faz com que os botões tentem preencher o espaço disponível na janela.
anchor="center": Alinha o botão no centro. Usa cordenada: n,s,e,w,ne,nw,se,sw

grid(): Posicionamento em grade (linhas e colunas)
btn.grid(row=0, column=1, padx=10, pady=10)
row e column: Definem a linha e a coluna onde o botão será colocado.
padx e pady: Adicionam preenchimento ao redor do botão, semelhante ao pack().

place(): Posicionamento absoluto
x e y: Especificam as coordenadas exatas onde o botão será posicionado dentro da janela, começando do canto superior esquerdo.
"""