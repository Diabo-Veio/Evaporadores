from Evap3E import *
import tkinter as tk
from tkinter import *
from tkinter import ttk

#-----------------------------#
############ DADOS ############
#-----------------------------#

#-----------------------------#
########### Tela ###########
#-----------------------------#
U1 = 2
parent = Tk()
parent.title("Evaporador NaOH de Triplo Efeito")

#frm = ttk.Frame(parent,width=600,height=300)
Calc = Button(parent, text="Calculate", command=lambda:loop("batata"))
Calc.grid(row=7, column=0,columnspan=4)

image = PhotoImage(file="imagem.png")
image_label = tk.Label(parent, image=image)
image_label.grid(row=0, column=0,columnspan=4)
##--------------------------------------------##
L_Tf = Label(parent, text = "Tf: ")
L_Tf.grid(row = 1, column = 0,sticky = E)
L_F = Label(parent, text = "F: ")
L_F.grid(row = 2, column = 0,sticky = E)
L_xf = Label(parent, text = "xf: ")
L_xf.grid(row = 3, column = 0,sticky = E)
L_Ps = Label(parent, text = "Ps: ")
L_Ps.grid(row = 4, column = 0,sticky = E)
L_P3 = Label(parent, text = "P3: ")
L_P3.grid(row = 5, column = 0,sticky = E)
L_x3 = Label(parent, text = "x3: ")
L_x3.grid(row = 1, column = 2,sticky = E)
L_U1 = Label(parent, text = "U1: ")
L_U1.grid(row = 2, column = 2,sticky = E)
L_U2 = Label(parent, text = "U2: ")
L_U2.grid(row = 3, column = 2,sticky = E)
L_U3 = Label(parent, text = "U3: ")
L_U3.grid(row = 4, column = 2,sticky = E)

E_Tf = Entry(parent)
E_Tf.grid(row = 1, column = 1, pady = 2,sticky = W)
E_F = Entry(parent)
E_F.grid(row = 2, column = 1, pady = 2,sticky = W)
E_xf = Entry(parent)
E_xf.grid(row = 3, column = 1, pady = 2,sticky = W)
E_Ps = Entry(parent)
E_Ps.grid(row = 4, column = 1, pady = 2,sticky = W)
E_P3 = Entry(parent)
E_P3.grid(row = 5, column = 1, pady = 2,sticky = W)
E_x3 = Entry(parent)
E_x3.grid(row = 1, column = 3, pady = 2,sticky = W)
E_U1 = Entry(parent)
E_U1.grid(row = 2, column = 3, pady = 2,sticky = W)
E_U2 = Entry(parent)
E_U2.grid(row = 3, column = 3, pady = 2,sticky = W)
E_U3 = Entry(parent)
E_U3.grid(row = 4, column = 3, pady = 2,sticky = W)
##--------------------------------------------##
tree=ttk.Treeview(parent,columns=range(3),height=10)
tree.grid(row=6, column=0,columnspan=4)

tree.heading('#0', text='Variável')
tree.heading('#1', text='Valor')
tree.heading('#2', text='Unidade')

parent.mainloop()