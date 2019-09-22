import sys
import os
import tkinter
import tkinter.messagebox
top=tkinter.Tk()
top.geometry('280x280')
top.title(' Flame system Analysis ')


def ethanol():
    os.system('C:\\Users\\shank\\Desktop\\flame\\ethanol.py')
def heptane():
    os.system('C:\\Users\\shank\\Desktop\\flame\\heptane.py')
def methanol():
    os.system('C:\\Users\\shank\\Desktop\\flame\\methanol.py')
def diesel():
    os.system('C:\\Users\\shank\\Desktop\\flame\\diesel.py')
def eh():
    os.system('C:\\Users\\shank\\Desktop\\flame\\ethanolheat.py')
def mh():
    os.system('C:\\Users\\shank\\Desktop\\flame\\methanolheat.py')    
def hh():
    os.system('C:\\Users\\shank\\Desktop\\flame\\heptaneheat.py')      
def dh():
    os.system('C:\\Users\\shank\\Desktop\\flame\\dieselheat.py')

A=tkinter.Button(top,text="ETHANOL",width=25,bg="orange",command= ethanol)
A.pack()


B=tkinter.Button(top,text="HEPTANE",width=25,bg="orange",command= heptane)
B.pack()

C=tkinter.Button(top,text="METHANOL",width=25,bg="orange",command= methanol)
C.pack()

D=tkinter.Button(top,text="DIESEL",width=25,bg="orange",command= diesel)
D.pack()

E=tkinter.Button(top,text="Heat map Ethanol",width=25,bg="orange",command= eh)
E.pack()

F=tkinter.Button(top,text="Heat map Methanol",width=25,bg="orange",command= mh)
F.pack()

H=tkinter.Button(top,text="Heat map Heptane",width=25,bg="orange",command= hh)
H.pack()

G=tkinter.Button(top,text="Heat map diesel",width=25,bg="orange",command= dh)
G.pack()

I = tkinter.Button(top, text='Stop', width=25,bg="orange", command=top.destroy)
I.pack()
top.mainloop()
