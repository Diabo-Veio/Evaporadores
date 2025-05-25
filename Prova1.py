from script import *
import tkinter as tk
from tkinter import *
from tkinter import ttk

#-----------------------------#
############ DADOS ############
#-----------------------------#

## Dados da alimentação ##
xf = 0.05
F = 38000 #Kg/h
Tf = 37.8 #°C
## Steam ##
Ps = 1.5/10.197 #Kgf/cm2 para MPa
## Alvo do Processo ##
P3 = 70/7501 #mmHg para Mpa -- Pressão no evap 3
x3 = 0.4
## Coef de troxca termica ##
U1 = 21338.4 #Kj/h*m2*C
U2 = 11547.84 #Kj/h*m2*C
U3 = 7782.24 #Kj/h*m2*C

#-----------------------------#
########### Tela ###########
#-----------------------------#

parent = tk.Tk()
parent.title("Evaporador NaOH de Triplo Efeito")

frm = ttk.Frame(parent,width=600,height=300)
ttk.Button(frm, text="Calculate", command=loop).grid(column=0)
ttk.Button(frm, text="Fechar", command=parent.destroy).grid(column=1)

image = PhotoImage(file="imagem.png")
image_label = tk.Label(parent, image=image)

tree=ttk.Treeview(parent,columns=range(3),height=10)


tree.heading('#0', text='Variável')
tree.heading('#1', text='Valor')
tree.heading('#2', text='Unidade')

image_label.pack(side="top")
tree.pack(padx = 5, pady = 5)
frm.pack()
parent.mainloop()