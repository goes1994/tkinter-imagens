from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from PIL import ImageTk, Image, ImageOps

import os 

def open_file():
    folder_patch = filedialog.askdirectory()

    if folder_patch:
        messagebox.showinfo(
            title='Abrindo diretório...',
            message=f'O diretório selecionado foi: {folder_patch}'
        )
    else:
        messagebox.showerror(
            title='Erro ao abrir diretório',
            message='Nehum diretório foi selecionado'

        )
        
    

root = Tk()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

#Titulo barra menu
root.title('Album')

#Lista os arquivos da pasta imagens
arquivos = os.listdir('imagens')

#Variavel para armazenar as imagens
imagens = []

#Variavel de controle de indices de imagem atual
imagem_atual = 0

#Percorer a lista de arquivos
for arquivo in arquivos:
    #Abre a imagem
    try:
        img = Image.open('imagens/' + arquivo)
    except:
        pass
    #Redimencionar imagem
    img = ImageOps.contain(img, (500, 500))
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
botao = Button(root, text='ANTERIOR', command=prev_Image, bg='black', fg='white', font=('Arial',10,'bold'))

botao.grid(column=0 , row=1, sticky= E + W)

botao = Button(root, text='PROXIMO', command=next_Image, bg='black', fg='white', font=('Arial',10,'bold'))

botao.grid(column=1 , row=1, sticky= E + W)

botao = Button(root, text='SAIR', command=root.quit, bg='black', fg='white', font=('Arial',10,'bold'))

botao.grid(column=2 , row=1, sticky= E + W)

root.bind('<Right>', lambda event: next_Image())
root.bind('<Left>', lambda event: prev_Image())
root.bind('<Escape>', lambda event: root.quit())


root.mainloop()