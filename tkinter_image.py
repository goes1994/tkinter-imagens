from tkinter import *

from PIL import ImageTk, Image

import os 

root = Tk()

#Lista os arquivos da pasta imagens
arquivos = os.listdir('imagens')

#Variavel para armazenar as imagens
imagens = []

#Percorer a lista de arquivos
for arquivo in arquivos:
    #Abre a imagem
    img = Image.open('imagens/' + arquivo)
    #Adiciona a imagem a lista
    imagens.append(ImageTk.PhotoImage(img))

#Exibe arquivos em um label
#arquivos_label = Label(root, text=arquivos)
#arquivos_label.pack()
#img = Image.open('imagens/meme.jpg')
#img_tk = ImageTk.PhotoImage(img)

img_label = Label(root, image=imagens [0])

img_label.pack()

root.mainloop()