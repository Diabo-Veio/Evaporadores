from Evap3E import *
import tkinter as tk
from tkinter import *
from tkinter import ttk

#-----------------------------#
########### Tela ###########
#-----------------------------#
variaveis = ['x1','x2','x3','A1','A2','A3','hl1','Hv1','hl2','Hv2','hl3','Hv3','T1','T2','T3']
unidades = ['-','-','-','m²','m²','m²','Kj/Kg','Kj/Kg','hlKj/Kg2','Kj/Kg','Kj/Kg','Kj/Kg','°C','°C','°C']

#-----------------------------#
########### Tela ###########
#-----------------------------#
#inicia a janela de interface grafica
parent = Tk()
parent.title("Evaporador NaOH de Triplo Efeito")

#region Imagem do sistema
image = PhotoImage(file="imagem.png")
image_label = tk.Label(parent, image=image)
image_label.grid(row=0, column=0,columnspan=4)
#endregion

#region Declaração de campos para input
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
#endregion

#region Atribuições de valores padrão
E_Tf.insert(END,37.8)
E_F.insert(END,38000)
E_xf.insert(END,0.05)
E_Ps.insert(END,1.5/10.197)
E_P3.insert(END,70/7501)
E_x3.insert(END,0.4)
E_U1.insert(END,21338.4)
E_U2.insert(END,11547.84)
E_U3.insert(END,7782.24)
#endregion

#region Tabela para mostrar resultados
tree=ttk.Treeview(parent,columns=range(3),height=15)
tree.grid(row=6, column=0,columnspan=4)
##Cabeçalho da tabela
tree.heading('#0', text='Variável')
tree.heading('#1', text='Valor')
tree.heading('#2', text='Unidade')

#endregion

#region Atribuição de variáveis
def valores():
    _Tf = float(E_Tf.get())
    _F = float(E_F.get())
    _xf = float(E_xf.get())
    _Ps = float(E_Ps.get())
    _P3 = float(E_P3.get())
    _x3 = float(E_x3.get())
    _U1 = float(E_U1.get())
    _U2 = float(E_U2.get())
    _U3 = float(E_U3.get())
    a = loop(_xf,_F,_Tf,_Ps,_P3,_x3,_U1,_U2,_U3)
    for i in a:
        tree.insert('', a.index(i), text= variaveis[a.index(i)], values=(i,unidades[a.index(i)]))
#endregion

#region Testes
Calc = Button(parent, text="Teste", command=lambda:print(E_x3.get()))
Calc.grid(row=7, column=3,columnspan=2)
#endregion

#region Botão para chamar o script de calculo
Calc = Button(parent, text="Calculate", command=lambda:valores())
Calc.grid(row=7, column=0,columnspan=2)
#endregion

parent.mainloop()