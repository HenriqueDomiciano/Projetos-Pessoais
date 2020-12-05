from tkinter import *
from tkinter import filedialog
from pytube import YouTube

def local_do_arquivo():
     e = filedialog.askdirectory()
     return e
def Youtube_download(local):
    global url 
    script = url.get()
    yt=YouTube(script)
    title=yt.title
    Tk.Label(root,text=title)

    valores = yt.streams.filter(only_audio=True).all()
    print(str(valores))


    yt.streams.get_by_itag(input("digite a itage"))

    yt.download(local)

    
root = Tk()


instructions=Label(root,text='digite a url do video ou da playlist').pack()
url = Entry(root)
url.pack()
local=Button(root,text="Aperte para escolher o diretorio",command=local_do_arquivo).pack()
botao=Button(root,text='Download',command = lambda :Youtube_download(local)).pack()

root.mainloop()