# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:49:06 2026

@author: 83837
"""

import numpy as np
import matplotlib.pyplot as plt
from figsc2 import pv
config = {
    "font.family":'Times New Roman',  
    "axes.unicode_minus": False 
}
from matplotlib import rcParams
rcParams.update(config)
font={"family":'Times New Roman','weight':'bold','size':20}
# ============================================
# 1. upper limit of the integral T
# ============================================
def MSD(pop,nM,lent):
  m7=[]
  m8=[]
  for i in range(lent):
    a=0
    b=0
    for j in range(nM*4+4):
        if j%4==2:
            a+=((j+2)/4)**2*(pop[j][i]) 
            b+=((j+2)/4)**2*(pop[j+1][i])
        elif j%4==0:
            a+=(j/4)**2*(pop[j][i])
            b+=(j/4)**2*(pop[j+1][i])         
    m7.append(a/nM) 
    m8.append(b/nM)
  return m7,m8

def time_raction(f,flag,threshold = 0.65,N=30,criteria=1e-6):
    data = np.load(f, allow_pickle=True)
    lent=len(data['tlist'])
    m1,m2=MSD(data['expect_values'],N,lent)
    pop=[]
    for i in range(lent): 
      if flag==True:
        #with dissipation,number of electron on A is computed
        pop.append(data['expect_values'][-1][i]+data['expect_values'][-2][i])          

    if flag==True:#with dissipation,number of electron on A is computed
        for i in range(lent):
            if pop[i]<threshold:
                a=i
        T_idx = a
        if pop[-1] < threshold:
            T_idx = lent - 1
# if not reached, take the final time
    elif flag==False:
        T_idx = lent - 1

    T = T_idx   
# ============================================
# 2. calculate eading-time fraction f
# ============================================
# +1 for up > down，-1 for down > up
    
    diff=[]
    for i in range(0,T,1):
        indicator_diff = (m1[i]-m2[i]>criteria).astype(float) - (m2[i]-m1[i]>criteria).astype(float)    
        diff.append(indicator_diff)

# Numerical integration (trapezoidal method), time step size dt=1
    integral = np.trapezoid(diff, dx=1)
    #integral = np.sum(diff)
    f = integral / (T)   

    print(f"领先时间分数 f = {f:.4f}")
    return f

D=[]
D.append(time_raction('results_lindblad_516.npz',False)) #G=0,longer time
D.append(time_raction('results_lindblad_519.npz',False)) #G=0.01
D.append(time_raction('results_lindblad_520.npz',False)) #G=0.03eV
D.append(time_raction('results_lindblad_521.npz',False)) #G=0.05eV
D.append(time_raction('results_lindblad_525.npz',False)) #G=0.075eV
D.append(time_raction('results_lindblad_522.npz',True)) #G=0.1eV
D.append(time_raction('results_lindblad_523.npz',True)) #G=0.2eV
D.append(time_raction('results_lindblad_524.npz',True)) #G=0.3eV
D.append(time_raction('results_lindblad_232.npz',True)) #G=0.4eV
D.append(time_raction('results_lindblad_114.npz',True)) #G=0.5eV
D.append(time_raction('results_lindblad_233.npz',True)) #G=0.6eV
#D.append(time_raction('results_lindblad_115.npz',True)) #G=0.7eV
D.append(time_raction('results_lindblad_234.npz',True)) #G=0.8eV
#D.append(time_raction('results_lindblad_116.npz',True)) #G=0.9eV
D.append(time_raction('results_lindblad_117.npz',True)) #G=1eV

#gamma_H=0.5meV
D.append(time_raction('results_lindblad_536.npz',False,criteria=1e-2)) #G=0,longer time
D.append(time_raction('results_lindblad_527.npz',True)) #G=0.01
D.append(time_raction('results_lindblad_528.npz',True)) #G=0.03eV
D.append(time_raction('results_lindblad_529.npz',True)) #G=0.05eV
D.append(time_raction('results_lindblad_530.npz',True)) #G=0.075eV
D.append(time_raction('results_lindblad_144.npz',True)) #G=0.1eV
D.append(time_raction('results_lindblad_534.npz',True)) #G=0.2eV
D.append(time_raction('results_lindblad_143.npz',True)) #G=0.3eV
D.append(time_raction('results_lindblad_533.npz',True)) #G=0.4eV
D.append(time_raction('results_lindblad_142.npz',True)) #G=0.5eV
D.append(time_raction('results_lindblad_531.npz',True)) #G=0.6eV
D.append(time_raction('results_lindblad_532.npz',True)) #G=0.8eV
D.append(time_raction('results_lindblad_139.npz',True)) #G=1eV

a=[0,0.01,0.03,0.05,0.075,0.1,0.2,0.3,0.4,0.5,0.6,0.8,1]
plt.plot(a,D[0:13],linestyle='solid',marker='o',linewidth=2.0,label='$\\Gamma_H=0$')
plt.plot(a,D[13:26],linestyle=':',marker='v',linewidth=2.0,label='$\\Gamma_H=0.5meV$')
plt.xlabel('$\\Gamma(eV)$',font,fontsize=20)
plt.ylabel('Leading-Time Fraction',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(frameon=False,prop=font,fontsize=20)

plt.tight_layout()
plt.savefig('figsd2.png',dpi=600,bbox_inches='tight')
plt.show()


a=[0.3,0.4,0.5,0.6,0.8,1]
totalpv=[]
totalpv.append(pv[0]*D[7])#0.3
totalpv.append(pv[1]*D[8])#0.4
totalpv.append(pv[2]*D[9])#0.5
totalpv.append(pv[3]*D[10])#0.6
totalpv.append(pv[5]*D[11])#0.8
totalpv.append(pv[7]*D[12])#1  

plt.plot(a,totalpv,linestyle='solid',marker='o',linewidth=2.0)
plt.xlabel('$\\Gamma(eV)$',font,fontsize=20)
plt.ylabel('Revised $P_v$',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#plt.legend(frameon=False,prop=font,fontsize=20)

plt.tight_layout()
plt.savefig('figsd3.png',dpi=600,bbox_inches='tight')
plt.show()