# coding=utf-8
import subprocess, shlex,os,sys ,Made_Folder ,getpass , threading
from subprocess import *
from Tkinter import *
from tkMessageBox import *

counter = 0
obj = Made_Folder.makeFolder()
obj.path_folder()
savepath=str(os.path.join(*["C:/Users/"+getpass.getuser()+"/Documents/PyROUTER/"]))
completeName=str(os.path.join(savepath+"router.txt"))
NameRede=str(os.path.join(savepath+"NameWifi.txt"))
connLISTA=str(os.path.join(savepath+"conn.txt"))
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
    sw = Label(root, text="                                                                                             ", font=(20))
    sw.pack()
    sw.grid(row=5, column=3, )
def writeconf ():
    namered = str(E3.get())
    EnPass = str(E4.get())
    RouterDef = os.path.join(*['netsh wlan set hostednetwork mode=allow ssid=' + namered + ' key=' + EnPass + ' keyusage=persistent'])
    NameDef = os.path.join(*[namered])
    file = open(completeName, 'w')#write the config of  the wifi to .txt
    file.write(RouterDef)
    file.close()
    file = open(NameRede, 'w') #Write  the name of the wifi to .txt
    file.write(NameDef)
    file.close()
def displaynameonload():
    file = open(NameRede)
    defDisplay = str(file.read())
    sw = Label(root, text="Rede: " + defDisplay, font=(20))
    sw.pack()
    sw.grid(row=5, column=3, )



def load():
    if os.path.isfile(completeName):
        file = open(completeName)
        definition=str(file.read())
        print(definition)
        subprocess.call(definition, shell=True)
        subprocess.call('netsh wlan start hostednetwork', shell=True)
        aload = showwarning('Connection start', 'configuracao previamente definida carregada com sucesso\n'+definition)
        displaynameonload();

    else:
        warload = showwarning('Warning', 'Configuration files does not exist yet')

def printVal():
    sw = Label(root, text="Rede: "+str(E3.get()), font=(20))
    sw.pack()
    sw.grid(row = 5, column = 3, )

def combine():
    Made_rot()
    writeconf()
    printVal()

def About():
    cpright=u'©'.encode('utf-8')
    ass = showinfo('Developer', 'Desenvolvido por Henrique Martins de Souza \n     Para Sugestões ou ajuda:\n\thsouzadev@gmail.com\n'+'\t'+cpright +'2017'+' H. Souza')

def ConfigOpen():
    if os.path.isfile(completeName):
        subprocess.call(['notepad.exe',completeName])
    else:
        warend = showwarning('Warning', 'Configuration files does not exist yet')

def connlist():
    log = open(connLISTA, 'w')
    log.flush()
    subprocess.call('netsh wlan show hostednetwork', stdout=log, shell=True)
    subprocess.Popen(["notepad.exe", connLISTA])

def count():
    global counter
    counter += 1
   # text=str(counter)


def refre():
    global op
    op=threading.Timer(900, refre)
    op.start()
    subprocess.call('netsh wlan stop hostednetwork', shell=True)
    subprocess.call('netsh wlan start hostednetwork', shell=True)
    #threading.Timer(900, refre).start()
    #print "Hello,: "+str(datetime.datetime.now().time())
def refreEND():
    op.cancel()
    #print "end,: "+str(datetime.datetime.now().time())

def reload():
    subprocess.call('netsh wlan stop hostednetwork', shell=True)
    ass = showwarning('Connection', 'reload')
    #.after(30000, lambda: ass.destroy())
    subprocess.call('netsh wlan start hostednetwork', shell=True)

def helpuser():
    netmsg="\aPara compartilhar sua conexão de internet com  o hotspot\a\n \n1º Central de Rede e Compartilhamento e clique em Alterar as configurações do adaptador.\n2º Clique com o botão direito em cima da conexão que você usa para se conectar à internet e selecione a opção Propriedades. \n3º Nas Propriedades, vá na aba Compartilhamento e marque a caixa Permitir que outros usuários da rede se conectem pela conexão desse computador à Internet e selecione o nome da conexão de rede que é usado pelo seu hotspot Salve as alterações."
    msguser = showinfo("Ajuda", netmsg)







root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff=False)

menu.add_cascade(label="Functions", menu=filemenu)

filemenu.add_command(label="Config", command=ConfigOpen)
filemenu.add_command(label="info Rede", command=connlist)
filemenu.add_command(label="Reiniciar", command=reload)
#comment for LG QE Team version
#filemenu.add_command(label="Refresh After 15 min", command=refre)
#filemenu.add_command(label="Stop Refresh", command=refreEND)
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Ajuda", menu=helpmenu)
helpmenu.add_command(label="Help", command=helpuser)
helpmenu.add_command(label="About", command=About)

#alop = count()

#print str(counter)

w = Label(root, text="",font=(20))
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

root.wm_iconbitmap(bitmap = 'icWifi.ico')
root.title("PyRouter v0.11")
root.resizable(width=False, height=False)
root.mainloop()