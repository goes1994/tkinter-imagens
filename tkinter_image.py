from tkinter import *

from PIL import ImageTk, Image, ImageOps

import os 

root = Tk()

root.title('Cadastro')

#Lista os arquivos da pasta imagens
arquivos = os.listdir('imagens')

#Variavel para armazenar as imagens
imagens = []

#Variavel de controle de indices de imagem atual
imagem_atual = 0

#Percorer a lista de arquivos
for arquivo in arquivos:
    #Abre a imagem
    img = Image.open('imagens/' + arquivo)
    #Redimencionar imagem
    img = ImageOps.contain(img, (300, 200))
    #Adiciona a imagem a lista
    imagens.append(ImageTk.PhotoImage(img))

#Exibe arquivos em um label
#arquivos_label = Label(root, text=arquivos)
#arquivos_label.pack()
#img = Image.open('imagens/meme.jpg')
#img_tk = ImageTk.PhotoImage(img)

img_label = Label(root, image=imagens[imagem_atual])

img_label.grid(column=0 , row=0, columnspan=3)

def prev_Image():
    global imagem_atual
    global img_label
    global imagens

#verifica se e a primeira imagem. se sim, volta para a ultima imagem
    if imagem_atual == 0:
        imagem_atual = len(imagens) -1
    else:
        imagem_atual -= 1

   #apaga a imagem atual 
    img_label.grid_forget()

   #exibe a nova imgame
    img_label = Label(root, image=imagens[imagem_atual])
    img_label.grid(column=0, row=0, columnspan=3)

def next_Image():

    global imagem_atual
    global img_label
    global imagens

#verifica se e a primeira imagem. se sim, volta para a ultima imagem
    if imagem_atual == len(imagens) -1:
        imagem_atual = 0
    else:
        imagem_atual += 1

   #apaga a imagem atual 
    img_label.grid_forget()

   #exibe a nova imgame
    img_label = Label(root, image=imagens[imagem_atual])
    img_label.grid(column=0, row=0, columnspan=3)

    pass

#Cria botao 
botao = Button(root, text='ANTERIOR', command=prev_Image)

botao.grid(column=0 , row=1)

botao = Button(root, text='PROXIMO', command=next_Image)

botao.grid(column=1 , row=1)

botao = Button(root, text='SAIR', command=root.quit)

botao.grid(column=2 , row=1)

root.mainloop()