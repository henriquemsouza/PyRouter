import subprocess, shlex,os,sys
from Tkinter import *
from tkMessageBox import *


def Made_rot():
    namered=str(E3.get())
    EnPass=str(E4.get())
    RouterDef=os.path.join(*['netsh wlan set hostednetwork mode=allow ssid='+namered+' key='+EnPass+' keyusage=persistent'])
    #RouterDef save to  on file txt  and mada is exists
    subprocess.call(RouterDef, shell=True)
    subprocess.call('netsh wlan start hostednetwork', shell=True)
    ass = showwarning('Connection start', 'Conectado')

def End_rot():
    subprocess.call('netsh wlan stop hostednetwork', shell=True)
    ass = showwarning('Connection end', 'Desconectado')
def writeconf ():
    namered = str(E3.get())
    EnPass = str(E4.get())
    RouterDef = os.path.join(*['netsh wlan set hostednetwork mode=allow ssid=' + namered + ' key=' + EnPass + ' keyusage=persistent'])
    file = open("router.txt", 'w')
    file.write(RouterDef)
    file.close()
def load():
    file = open("router.txt")
    definition=str(file.read())
    print(definition)
    subprocess.call(definition, shell=True)
    subprocess.call('netsh wlan start hostednetwork', shell=True)
    ass = showwarning('Connection start', 'configuracao previamente definida carregada com sucesso')

def combine():
    Made_rot()
    writeconf()


root = Tk()

w = Label(root, text="PyRouter",font=(20))
w.pack()
w.grid(row=1, column=3)
sp = Label(root, text="")
sp.pack()
sp.grid(row=0, column=1)
nrede = Label(root, text="Nome da  rede")
nrede.pack()
nrede.grid(row=2, column=2)
sred = Label(root, text="Senha da rede")
sred.pack()
sred.grid(row=3, column=2)


Button(root, text='Iniciar', command=combine).grid(row=4, column=3, sticky=W, pady=5)
Button(root, text='Desconectar', command=End_rot).grid(row=4, column=2, sticky=W, pady=5)
Button(root, text='Carregar', command=load).grid(row=5, column=2, sticky=W, pady=5)

E3 = Entry(root)
E3["width"]=100
E3.grid(row=2, column=3)
E4 = Entry(root)
E4["width"]=100
E4.grid(row=3, column=3)

root.geometry("700x200")

root.wm_iconbitmap('icWifi.ico')
root.title("PyRouter v0.2")
root.resizable(width=False, height=False)
root.mainloop()