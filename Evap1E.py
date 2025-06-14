import numpy as np
from iapws import IAPWS97 as tb
import sympy
from sympy.solvers import solve
from sympy import Eq

#-----------------------------#
############ DADOS ############
#-----------------------------#


def zerando():
    global L_,V_,T_,Tsat_,EPE_,hf_,hl_,Hv_,S_,q_,A_,Economia_,θ_,Cp_,λs_
    L_=V_=T_=Tsat_=EPE_=hf_=hl_=Hv_=S_=q_=A_=Economia_=θ_=Cp_=λs_=0

def Balanço_de_Massa():
    global L_,V_
    L_ = (F_*xf_)/xl_
    V_ = F_-L_

def Ponto_de_Eb():
    global T_,Tsat_,EPE_,Ts_
    Tsat_ = tb(P=P_,x=0.000001).T-273.15
    EPE_ = (271.3627*xl_**2 - 9.419608*xl_ + 0.1419526*xl_*(32+Tsat_*(9/5)))*5/9                                     ## °C - Elevação do Ponto de Ebulição
    T_ = Tsat_+EPE_
    Ts_ = tb(P=Ps_,x=0.999999).T-273.15

def entalpias():
    global hf_,hl_,Hv_,λs_,θ_,Cp_
    hf_ = (-10.25 - 319.591837*xf_ + 939.795918*xf_**2 + 0.963929*(32+Tf_*(9/5)) - 0.335714*xf_*(32+Tf_*(9/5)))*2.326  ## Kj/Kg - Entalpia da Alimentação
    
    hl_ = (-10.25 - 319.591837*xl_ + 939.795918*xl_**2 + 0.963929*(32+T_*(9/5)) - 0.335714*xl_*(32+T_*(9/5)))*2.326  ## Kj/Kg - Entalpia do Líquido
    θ_ = (T_+273.15)/1000
    Cp_ = 1.79+0.107*θ_+0.586*θ_**2-0.2*θ_**3
    Hv_ = tb(T=Tsat_+273.15,x=0.9999999).h + Cp_*(EPE_)
    
    λs_ = (1094.002 - 0.57342487*(32+Ts_*(9/5)) + 1.5049887E-4*(32+Ts_*(9/5))**2 - 9.3061810E-7*(32+Ts_*(9/5))**3)*2.326

def sistema_final():
    global S_,q_,A_,Economia_
    S_ = ((L_*hl_)+(V_*Hv_)-(F_*hf_))/λs_
    q_ = S_*(λs_*1/(60*60))
    A_ = (q_*1000)/(U_*(Ts_-T_))
    Economia_ = V_/S_

def loop_1(xf,_F,_Tf,_Ps,_P,_xl,_U,):
    global F_,Tf_,P_,Ps_,xf_,xl_,U_
    F_ = _F
    Tf_ = _Tf
    P_ = _P
    Ps_ = _Ps
    xf_ = xf
    xl_ = _xl
    U_ = _U
    zerando()
    Balanço_de_Massa()
    Ponto_de_Eb()
    entalpias()
    sistema_final()
    return S_,Economia_,A_,hl_,Hv_,T_