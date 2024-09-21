# import RPi.GPIO as GPIO
# import time 
# from tkinter import *

# janela = Tk()
# janela.geometry("800x600+0+0")

# texto1 = Label(janela, text="Distancia",font="Arial 40")
# texto1.place(x=300,y=100)

# texto2 = Label(janela, text="Distancia entre o sensor eo objeto",font="Arial 35",foreground="blue")
# texto2.place(x=20,y=20)

# imagem1 = PhotoImage(file="objeto.png")
# imagem2 = PhotoImage(file="sensor_ultra.png")

# label_sensor = Label(janela,image=imagem2)
# label_sensor.place(x=600,y=300)

# label_objeto = Label(janela,image=imagem1)
# label_objeto.place(x=200,y=300)

# GPIO.setmode(GPIO.BOARD)
# TRIGGER = 11
# ECHO = 12

# GPIO.setup(TRIGGER,GPIO.OUT)
# GPIO.setup(ECHO,GPIO.IN)
# time.sleep(1)

# try:
# 	while True:
# 		GPIO.output(TRIGGER,True)
# 		time.sleep(0.00001)  #  pulso de 10 micro-segundos
# 		GPIO.output(TRIGGER,False)

# 		while GPIO.input(ECHO) == 0:
# 			tempo_inicial = time.time()

# 		while GPIO.input(ECHO) == 1:
# 			tempo_final = time.time()

# 		tempo_total = tempo_final - tempo_inicial
# 		distancia = (tempo_total * 34000)/2

# 		if distancia <=5:
# 			label_objeto.place(x=450,y=300)
# 		elif distancia > 5 and distancia <= 10:
# 			label_objeto.place(x=400,y=300)
# 		elif distancia > 10 and distancia <= 15:
# 			label_objeto.place(x=350,y=300)
# 		elif distancia > 15 and distancia <= 20:
# 			label_objeto.place(x=300,y=300)
# 		elif distancia > 20 and distancia <= 25:
# 			label_objeto.place(x=250,y=300)
# 		elif distancia > 25 and distancia <= 30:
# 			label_objeto.place(x=200,y=300)
# 		elif distancia > 30 and distancia <= 35:
# 			label_objeto.place(x=150,y=300)
# 		elif distancia > 35 and distancia <= 40:
# 			label_objeto.place(x=100,y=300)
# 		else:
# 			label_objeto.place(x=50,y=300)

# 		texto1['text'] = str(round(distancia,1)) + ' cm'
# 		janela.update()
# 		time.sleep(0.1)
# except KeyboardInterrupt:
# 	GPIO.cleanup()



