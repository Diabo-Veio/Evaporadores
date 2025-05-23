import numpy as np
from scipy.optimize import minimize
from iapws import IAPWS97 as tb
import sympy
from sympy.solvers import solve
from sympy import Eq


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
x3 = 0.5
## Coef de troxca termica ##
U1 = 21338.4 #Kj/h*m2*C
U2 = 11547.84 #Kj/h*m2*C
U3 = 7782.24 #Kj/h*m2*C

#-----------------------------#
##### Iniciando Variáveis #####
#-----------------------------#

## Frações de Soluto ##
x = np.zeros(4)
x[0]= xf 
x[3]= x3 
#Entalpia
hl1 = hl2 = hl3 = 0
hd1 = hd2 = hd3 = 0
Hv1 = Hv2 = Hv3 = 0
#Vapor
V1 = V2 = V3 = 0
#Liquido
L1 = L2 = L3 = 0
#Temperaturas
T1 = T2 = T3 = Ts = 0
Td1 = Td2 = Td3 = 0
#Elevação do Ponto de Ebulição
EPE1 = EPE2 = EPE3 = 0
#θ para caluco de Cp
θ1 = θ2 = θ3 = 0
#Veriáveis Pontuais
Tsat3 = 0
ΔT = 0
λs = 0
SomaVi = 0
S = 0
## Variáveis para resolução dos sistemas ##
ΔT1 , ΔT2 , ΔT3 = sympy.symbols('ΔT1 , ΔT2 , ΔT3')
s , v1 , v2 = sympy.symbols('s , v1 , v2')
## Distribuição de Vapores ##
L3 = (F*x[0])/x[3]
SomaVi = F-L3
V1=V2=V3=SomaVi/3
desv = np.zeros(3)
##Bool
refazer_T = True
refazer_A = True

##Áreas
desv_A = np.zeros(3)


def Balanco_de_Massa():
    global V1,V2,V3,SomaVi,L1,L2,L3,F
    ## Efeito 1 ##
    L1 = F-V1
    x[1] = (F*x[0])/L1
    ## Efeito 2 ##
    L2 = L1-V2
    x[2] = (L1*x[1])/L2

def Levantamento_de_Dados():
    global Ts,hf,Hv3,hl3,EPE3,Tsat3,T3,λs

    ##-------## 
    ## Steam ##
    ##-------##

    Steam = tb(P=Ps,x=0.9999)
    Ts = (Steam.T-273.15)
    λs = (1094.002 - 0.57342487*(32+Ts*(9/5)) + 1.5049887E-4*(32+Ts*(9/5))**2 - 9.3061810E-7*(32+Ts*(9/5))**3)*2.326
    
    ##-------------##
    ## Alimentação ##
    ##-------------##

    hf = (-10.25 - 319.591837*x[0] + 939.795918*x[0]**2 + 0.963929*(32+Tf*(9/5)) - 0.335714*x[0]*(32+Tf*(9/5)))*2.326  ## Kj/Kg - Entalpia da Alimentação
    
    ##----------##
    ## Produtos ##
    ##----------##

    # T #
    Tsat3 = tb(P=P3,x=0.9999).T - 273                                                                                   ## °C - Temperatura do Vapor Saturado na Pressão do Evap 3
    EPE3 = (271.3627*x[3]**2 - 9.419608*x[3] + 0.1419526*x[3]*(32+Tsat3*(9/5)))*5/9                                     ## °C - Elevação do Ponto de Ebulição
    T3 = Tsat3+EPE3                                                                                                     ## °C - Temperatura do Evap 3
    # H #
    hl3 = (-10.25 - 319.591837*x[3] + 939.795918*x[3]**2 + 0.963929*(32+T3*(9/5)) - 0.335714*x[3]*(32+T3*(9/5)))*2.326  ## Kj/Kg - Entalpia do Líquido 3
    Hv3 = tb(P=P3,T=T3+273.15).h                                                                                        ## Kj/Kg - Entalpia do Vapor 3

def DeltaT():
    global EPE1,EPE2,ΔT
    T1 = Tsat3+2*((Ts-Tsat3)/3)
    T2 = Tsat3+((Ts-Tsat3)/3)
    EPE1 = (271.3627*x[1]**2 - 9.419608*x[1] + 0.1419526*x[1]*(32+T1*(9/5)))*5/9
    EPE2 = (271.3627*x[2]**2 - 9.419608*x[2] + 0.1419526*x[2]*(32+T2*(9/5)))*5/9
    ΔT = (Ts)-Tsat3-(EPE1+EPE2+EPE3)

def Distribuicao_DeltaT():
    global output1
    #ΔT#
    eq1 = Eq(ΔT1-(U3/U1)*ΔT3,0)
    eq2 = Eq(ΔT2-(U3/U2)*ΔT3,0)
    eq3 = Eq(ΔT3+ΔT1+ΔT2,ΔT)
    output1 = solve([eq1,eq2,eq3],ΔT1,ΔT2,ΔT3,dict=True)

def Balanco_de_Energia():
    global desv,output2,S,Hv1,hl1,Hv2,hl2,hd2,hd3

    ##--------------##
    ## Temperatura ###
    ##--------------##

    #Efeito 1
    T1 = Ts - output1[0][ΔT1]
    Td1 = Ts
    #Efeito 2
    T2 = T1 - EPE1 - output1[0][ΔT2]
    Td2 = T1 - EPE1

    ##----------##
    ## Entalpia ##
    ##----------##

    #Efeito 1
    θ1 = T1/1000
    Cp1 = 1.79+0.107*θ1+0.586*θ1**2-0.2*θ1**3
    Hv1 = tb(T=T1+273.15,x=0.999999).h + Cp1*(EPE1)
    hl1 = (-10.25 - 319.591837*x[1] + 939.795918*x[1]**2 + 0.963929*(32+T1*(9/5)) - 0.335714*x[1]*(32+T1*(9/5)))*2.326  ## Kj/Kg - Entalpia do Líquido 1
    #Efeito 2
    θ2 = T2/1000
    Cp2 = 1.79+0.107*θ2+0.586*θ2**2-0.2*θ2**3
    Hv2 = tb(T=T2+273.15,x=0.999999).h + Cp2*(EPE2)
    hl2 = (-10.25 - 319.591837*x[2] + 939.795918*x[2]**2 + 0.963929*(32+T2*(9/5)) - 0.335714*x[2]*(32+T2*(9/5)))*2.326  ## Kj/Kg - Entalpia do Líquido 2
    hd2 = tb(T=(T1-EPE1)+273.15,x=0.0000001).h
    #Efeito 3
    hd3 = tb(T=(T2-EPE2)+273.15,x=0.0000001).h

    ##---------##
    ## Sistema ##
    ##---------##

    #Efeito 1
    eq1 = Eq(F*hf+s*λs-(F-v1)*hl1-v1*Hv1,0)
    #Efeito 2
    eq2 = Eq((F-v1)*hl1+v1*(Hv1-hd2)-(F-v1-v2)*hl2-v2*Hv2,0)
    #Efeito 3
    eq3 = Eq((F-v1-v2)*hl2+v2*(Hv2-hd3)-(F-v1-v2-V3)*hl3-((SomaVi-(v1+v2))*Hv3),0)
    #Resolução
    output2 = solve([eq1,eq2,eq3],v1,v2,s,dict=True)
    S = output2[0][s]
    desv[0] = np.abs(output2[0][v1]-V1)/V1
    desv[1] = np.abs(output2[0][v2]-V2)/V2
    desv[2] = np.abs((SomaVi - (output2[0][v1]+ output2[0][v2]))-V3)/V3
    
def Areas():
    global A1,A2,A3,output1,refazer_A
    #Efeito 1
    A1 = (S*λs)/(U1*output1[0][ΔT1])
    #Efeito 2
    A2 = (V1*(Hv1-hd2))/(U2*output1[0][ΔT2])
    #Efeito 3
    A3 = (V2*(Hv2-hd3))/(U3*output1[0][ΔT3])

    desv_A[0] = np.abs(A1-A2)/A1
    desv_A[1] = np.abs(A2-A3)/A2
    desv_A[2] = np.abs(A1-A3)/A3

    if(desv_A[0] > 0.05 or desv_A[1] > 0.05 or desv_A[2] > 0.05):
        A_media = (A1*output1[0][ΔT1]+A2*output1[0][ΔT2]+A3*output1[0][ΔT3])/(output1[0][ΔT1]+output1[0][ΔT2]+output1[0][ΔT3])
        output1[0][ΔT1] = (output1[0][ΔT1]*A1)/A_media
        output1[0][ΔT2] = (output1[0][ΔT2]*A2)/A_media
        output1[0][ΔT3] = (output1[0][ΔT3]*A3)/A_media
    else:
        refazer_A = False

while refazer_T:
    Balanco_de_Massa()
    Levantamento_de_Dados()
    DeltaT()
    Distribuicao_DeltaT()
    Balanco_de_Energia()

    V1 = output2[0][v1]
    V2 = output2[0][v2]
    V3 = (SomaVi - (output2[0][v1]+ output2[0][v2]))

    if(desv[0] < 0.05 and desv[0] < 0.05 and desv[0] < 0.05):
        refazer_T = False
        Areas()
        while refazer_A:
            Balanco_de_Energia()
            Areas()

print(x)






    