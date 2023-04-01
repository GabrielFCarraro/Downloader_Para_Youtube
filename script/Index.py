from tkinter import *
from pytube import YouTube,Playlist
import PIL
import pyperclip
import os

#DEF JANELA
janela = Tk()
janela.title('Youtube Downloader')
janela.iconbitmap('ico/ico.ico')
janela.geometry('650x320')
janela.resizable(FALSE, FALSE)
janela_img = PhotoImage(file = 'png/layout.png') 
fundo_janela = Label(janela, image = janela_img)
fundo_janela.pack()



#GAMBIARRAS
url = 0
resolucao = 0
quality = 0

#=============================================================DEFS=============================================================#


#def qualidades
def mp3():
    global quality
    quality = 'mp3'

def mp4():
    global quality
    quality = 'mp4'   

#def resoluções
def quatrok():
    global resolucao
    resolucao = str('2160p')


def qhd():
    global resolucao
    resolucao = str('1440p')


def fhd():
    global resolucao
    resolucao = str('1080p')


def hd():
    global resolucao
    resolucao = str('720p')


def tres_seis_zero():
    global resolucao
    resolucao = str('360p')


def quatro_oito_zero():
    global resolucao
    resolucao = str('480p')


#def download
def download():
    url = str(entry_colar.get())
    yt = YouTube(url)
    if "playlist" in entry_colar.get() and quality == 'mp4':
        stream = yt.streams.get_by_resolution(resolucao)
        stream.download(output_path = 'playlist')
    elif "playlist" in entry_colar.get() and quality == 'mp3':  
        stream = yt.streams.get_audio_only()
        stream.download(output_path = 'playlist')
    else:
        if quality == 'mp4': 
            stream = yt.streams.get_by_resolution(resolucao)
            stream.download()
        else:
            stream = yt.streams.get_audio_only()
            stream.download()   
    
    
#COLOCAR ESCRITA NO ENTRY
def entry_colar_click (event):
    if entry_colar.get() == 'Cole o link do video que deseja baixar':
        entry_colar.delete(0, 'end')
        entry_colar.insert(0, '')

def entry_colar_outclick (event):
    if entry_colar.get() == '':
        entry_colar.insert(0, 'Cole o link do video que deseja baixar')       
               

#BOTÃO COLAR
def paste():
    colar = pyperclip.paste()
    CAMPOCOLAR.set(colar)

#==========================================================BOTÕES E ETC=======================================================#

#CAMPO COPY
CAMPOCOLAR = StringVar()
entry_colar = Entry(janela, textvariable = CAMPOCOLAR, border = 0, font = 'Serif 15', width = 37)
entry_colar.place(x = 98, y = 73)
entry_colar.insert(0, 'Cole o link do video que deseja baixar')
entry_colar.bind('<FocusIn>', entry_colar_click)
entry_colar.bind('<FocusOut>', entry_colar_outclick)

#BOTÃO COLAR
bt_colar = PhotoImage(file = "png/buttons/btn_colar.png")
btn_colar = Button(janela, image = bt_colar, border = 0, height = 32, width = 36, command = paste)
btn_colar.place(x = 516, y = 70)

#BOTÃO 4K
bt_4k = PhotoImage(file = 'png/buttons/btn_4k.png')
btn_4k = Button(janela, image = bt_4k, border = 0, height = 23, width = 70 )
btn_4k.place(x = 8, y = 173)

#BOTÃO 2,5K
bt_2k = PhotoImage(file = 'png/buttons/btn_2k.png')
btn_2k = Button(janela, image = bt_2k, border = 0, height = 23, width = 70)
btn_2k.place(x = 90, y = 173)

#BOTÃO 1080P
bt_fhd = PhotoImage(file = 'png/buttons/btn_fhd.png')
btn_fhd = Button(janela, image = bt_fhd, border = 0, height = 23, width = 70, command = fhd)
btn_fhd.place(x = 8, y = 206)

#BOTÃO 720P
bt_hd = PhotoImage(file = 'png/buttons/btn_hd.png')
btn_hd = Button(janela, image  = bt_hd, border = 0, height = 23, width = 70, command = hd)
btn_hd.place(x = 90, y = 206)

#BOTÃO 480P
bt_480p =  PhotoImage(file = 'png/buttons/btn_480p.png')
btn_480p = Button(janela, image = bt_480p, border = 0, height = 23, width = 70, command = quatro_oito_zero)
btn_480p.place(x = 8, y = 239)

#BOTÃO 360P
bt_360p = PhotoImage(file = 'png/buttons/btn_360p.png')
btn_360p = Button(janela, image = bt_360p, border = 0, height = 23, width = 70, command = tres_seis_zero)
btn_360p.place(x = 90, y = 239)

#BOTÃO MP4
bt_mp4 = PhotoImage(file = 'png/buttons/btn_mp4.png')
btn_mp4 = Button(janela, image = bt_mp4, border = 0, height = 23, width = 70, command = mp4)
btn_mp4.place(x = 490, y = 173)

#BOTÃO MP3
bt_mp3 = PhotoImage(file = 'png/buttons/btn_mp3.png')
btn_mp3 = Button(janela, image = bt_mp3, border = 0, height = 23, width = 70, command = mp3)
btn_mp3.place(x = 571, y = 173)

#BOTÃO DOWNLOAD
bt_down = PhotoImage(file = 'png/buttons/btn_download.png')
btn_down = Button(janela, image = bt_down, border = 0, height = 36, width = 161, command = download)
btn_down.place(x = 244, y = 274)


janela.mainloop() 