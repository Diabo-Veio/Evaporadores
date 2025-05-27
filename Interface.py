import tkinter as tk
from tkinter import *
from tkinter import ttk
from Evap3E import *
from Evap1E import *
 
class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
 
        # initializing frames to an empty array
        self.frames = {}  
 
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Tripo_Efeito, Simples_Efeito):
 
            frame = F(container, self)
 
            # initializing frame of that object from
            # Tripo_Efeito, Simples_Efeito, respectively with 
            # for loop
            self.frames[F] = frame 
 
            frame.grid(row = 0, column = 0, sticky ="nsew")
 
        self.show_frame(Tripo_Efeito)
 
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
 
# first window frame startpage
 
class Tripo_Efeito(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        #-----------------------------#
        ### Variaveis para treeview ###
        #-----------------------------#
        variaveis = ['S','V1','V2','V3','x1','x2','T1','T2','A1','A2','A3','hl1','Hv1','hl2','Hv2','hl3','Hv3','Economia']
        unidades = ['Kg/h','Kg/h','Kg/h','Kg/h','-','-','°C','°C','m²','m²','m²','Kj/Kg','Kj/Kg','Kj/Kg','Kj/Kg','Kj/Kg','Kj/Kg','-']
        #-----------------------------#
        ########### Tela ###########
        #-----------------------------#

        #region Imagem do sistema
        self.image = PhotoImage(file="Triplo_E.png")
        self.image_label = Label(self, image=self.image)
        self.image_label.grid(row=0, column=0,columnspan=5)
        #endregion

        #region Declaração de campos para input
        ##Decalaraão de Etiquetas
        L_Tf = Label(self, text = "Tf: ")
        L_Tf.grid(row = 1, column = 0,sticky = E)
        L_F = Label(self, text = "F: ")
        L_F.grid(row = 2, column = 0,sticky = E)
        L_xf = Label(self, text = "xf: ")
        L_xf.grid(row = 3, column = 0,sticky = E)
        L_Ps = Label(self, text = "Ps: ")
        L_Ps.grid(row = 4, column = 0,sticky = E)
        L_P3 = Label(self, text = "P3: ")
        L_P3.grid(row = 5, column = 0,sticky = E)
        L_x3 = Label(self, text = "     x3: ")
        L_x3.grid(row = 1, column = 2,sticky = E)
        L_U1 = Label(self, text = "     U1: ")
        L_U1.grid(row = 2, column = 2,sticky = E)
        L_U2 = Label(self, text = "     U2: ")
        L_U2.grid(row = 3, column = 2,sticky = E)
        L_U3 = Label(self, text = "     U3: ")
        L_U3.grid(row = 4, column = 2,sticky = E)
        ##Decalaraão dos Campos
        E_Tf = Entry(self)
        E_Tf.grid(row = 1, column = 1, pady = 2,sticky = W)
        E_F = Entry(self)
        E_F.grid(row = 2, column = 1, pady = 2,sticky = W)
        E_xf = Entry(self)
        E_xf.grid(row = 3, column = 1, pady = 2,sticky = W)
        E_Ps = Entry(self)
        E_Ps.grid(row = 4, column = 1, pady = 2,sticky = W)
        E_P3 = Entry(self)
        E_P3.grid(row = 5, column = 1, pady = 2,sticky = W)
        E_x3 = Entry(self)
        E_x3.grid(row = 1, column = 3, pady = 2,sticky = W)
        E_U1 = Entry(self)
        E_U1.grid(row = 2, column = 3, pady = 2,sticky = W)
        E_U2 = Entry(self)
        E_U2.grid(row = 3, column = 3, pady = 2,sticky = W)
        E_U3 = Entry(self)
        E_U3.grid(row = 4, column = 3, pady = 2,sticky = W)
        ##Decalaraão de Etiquetas de unidade
        U_Tf = Label(self, text = "°C")
        U_Tf.grid(row = 1, column = 2,sticky = W)
        
        U_F = Label(self, text = "Kg/h")
        U_F.grid(row = 2, column = 2,sticky = W)

        U_xl = Label(self, text = "-")
        U_xf = Label(self, text = "-")
        U_xf.grid(row = 3, column = 2,sticky = W)
        U_xl.grid(row = 1, column = 4,sticky = W)

        U_P = Label(self, text = "Mpa")
        U_Ps = Label(self, text = "Mpa")
        U_Ps.grid(row = 4, column = 2,sticky = W)
        U_P.grid(row = 5, column = 2,sticky = W)

        U_U1 = Label(self, text = "Kj/h*m²")
        U_U2 = Label(self, text = "Kj/h*m²")
        U_U3 = Label(self, text = "Kj/h*m²")
        U_U1.grid(row = 2, column = 4, pady = 2,sticky = W)
        U_U2.grid(row = 3, column = 4, pady = 2,sticky = W)
        U_U3.grid(row = 4, column = 4, pady = 2,sticky = W)
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

        #region Declaração da tabela para mostrar resultados
        tree=ttk.Treeview(self,columns=range(3),height=15)
        tree.grid(row=6, column=0,columnspan=5)
        ##Cabeçalho da tabela
        tree.heading('#0', text='Variável')
        tree.heading('#1', text='Valor')
        tree.heading('#2', text='Unidade')
        #endregion

        #region Roda o programa e exibe os valores
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
            tree.delete(*tree.get_children())
            for i in a:
                tree.insert('', a.index(i), text= variaveis[a.index(i)], values=(i,unidades[a.index(i)]))
                
        #endregion

        #region Botão para chamar o script de calculo
        Calc = Button(self, text="Calculate", command=lambda:valores())
        Calc.grid(row=7, column=0,columnspan=2)

        button1 = Button(self, text ="Simples Efeito", command = lambda : controller.show_frame(Simples_Efeito))
        button1.grid(row=7, column=3,columnspan=2)
        #endregion
 
# second window frame Simples_Efeito 
class Simples_Efeito(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        #-----------------------------#
        ### Variaveis para treeview ###
        #-----------------------------#
        variaveis = ['S','Economia','A','hl','Hv','T']
        unidades = ['Kg/s','-','m²','Kj/Kg','Kj/Kg','°C']
        #-----------------------------#
        ########### Tela ###########
        #-----------------------------#

        #region Imagem do sistema
        self.image = PhotoImage(file="Simples_E.png")
        self.image_label = Label(self, image=self.image)
        self.image_label.grid(row=0, column=0,columnspan=5)
        #endregion

        #region Declaração de campos para input
        ##Decalaraão de Etiquetas de campo
        L_Tf = Label(self, text = "Tf: ")
        L_Tf.grid(row = 1, column = 0,sticky = E)
        L_F = Label(self, text = "F: ")
        L_F.grid(row = 2, column = 0,sticky = E)
        L_xf = Label(self, text = "xf: ")
        L_xf.grid(row = 3, column = 0,sticky = E)
        L_Ps = Label(self, text = "Ps: ")
        L_Ps.grid(row = 4, column = 0,sticky = E)
        L_P = Label(self, text = "P: ")
        L_P.grid(row = 1, column = 2,sticky = E)
        L_xl = Label(self, text = "x3: ")
        L_xl.grid(row = 2, column = 2,sticky = E)
        L_U = Label(self, text = "U1: ")
        L_U.grid(row = 3, column = 2,sticky = E)
        ##Decalaraão dos Campos
        E_Tf = Entry(self)
        E_Tf.grid(row = 1, column = 1,sticky = W)
        E_F = Entry(self)
        E_F.grid(row = 2, column = 1,sticky = W)
        E_xf = Entry(self)
        E_xf.grid(row = 3, column = 1,sticky = W)
        E_Ps = Entry(self)
        E_Ps.grid(row = 4, column = 1,sticky = W)
        E_P = Entry(self)
        E_P.grid(row = 1, column = 3,sticky = W)
        E_xl = Entry(self)
        E_xl.grid(row = 2, column = 3,sticky = W)
        E_U = Entry(self)
        E_U.grid(row = 3, column = 3,sticky = W)
        ##Decalaraão de Etiquetas de unidade
        U_Tf = Label(self, text = "°C")
        U_Tf.grid(row = 1, column = 2,sticky = W)
        U_F = Label(self, text = "Kg/h")
        U_F.grid(row = 2, column = 2,sticky = W)
        U_xf = Label(self, text = "-")
        U_xf.grid(row = 3, column = 2,sticky = W)
        U_Ps = Label(self, text = "Mpa")
        U_Ps.grid(row = 4, column = 2,sticky = W)
        U_P = Label(self, text = " Mpa")
        U_P.grid(row = 1, column = 4,sticky = W)
        U_xl = Label(self, text = "-")
        U_xl.grid(row = 2, column = 4,sticky = W)
        U_U = Label(self, text = " W/m²")
        U_U.grid(row = 3, column = 4,sticky = W)
        ##--------------------------------------------##
        #endregion

        #region Atribuições de valores padrão
        E_Tf.insert(END,60)
        E_F.insert(END,4536)
        E_xf.insert(END,0.2)
        E_Ps.insert(END,0.1724)
        E_P.insert(END,0.0117)
        E_xl.insert(END,0.5)
        E_U.insert(END,1560)
        #endregion

        #region Declaração da tabela para mostrar resultados
        tree=ttk.Treeview(self,columns=range(3),height=19)
        tree.grid(row=5, column=0,columnspan=5)
        ##Cabeçalho da tabela
        tree.heading('#0', text='Variável')
        tree.heading('#1', text='Valor')
        tree.heading('#2', text='Unidade')
        #endregion

        #region Roda o programa e exibe os valores
        def valores():
            _Tf = float(E_Tf.get())
            _F = float(E_F.get())
            _xf = float(E_xf.get())
            _Ps = float(E_Ps.get())
            _P = float(E_P.get())
            _xl = float(E_xl.get())
            _U = float(E_U.get())
            a = loop_1(_xf,_F,_Tf,_Ps,_P,_xl,_U,)
            tree.delete(*tree.get_children())
            for i in a:
                tree.insert('', a.index(i), text= variaveis[a.index(i)], values=(i,unidades[a.index(i)]))
                
        #endregion

        #region Botão para chamar o script de calculo
        Calc = Button(self, text="Calculate", command=lambda:valores())
        Calc.grid(row=6, column=0,columnspan=2)

        
        button1 = ttk.Button(self, text ="Tripo_Efeito",command = lambda : controller.show_frame(Tripo_Efeito))
        button1.grid(row=6, column=3,columnspan=2)
# Driver Code
app = tkinterApp()
app.mainloop()