# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:20:10 2026

@author: 83837
"""

import numpy as np
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
config = {
    "font.family":'SimHei',  
    "axes.unicode_minus": False 
}
from matplotlib import rcParams
rcParams.update(config)
font={"family":'Times New Roman','weight':'bold','size':20}

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

data = np.load('results_lindblad_566.npz', allow_pickle=True) #single strand
data2 = np.load('results_lindblad_565.npz', allow_pickle=True) #single strand
lent=len(data['tlist'])
x=[]
for i in range(0,lent,1):
   x.append(i*27.211*2.419/100/0.12*0.5) 

m1u,m1d=MSD(data['expect_values'],30,lent)
m2u,m2d=MSD(data2['expect_values'],30,lent)

plt.plot(x,m1u,'--',linewidth=2.0,label='$\\uparrow$, no SOC')
plt.plot(x,m1d,':',linewidth=2.0,label='$\\downarrow$, no SOC')
plt.plot(x,m2u,linewidth=2.0,label='$\\uparrow$,$t_{SO}$=20meV')
plt.plot(x,m2d,'-.',linewidth=2.0,label='$\\downarrow$,$t_{SO}$=20meV')

plt.title('single chain DNA',font,fontsize=20)
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(frameon=False,prop=font,fontsize=20)

plt.tight_layout()
plt.savefig('figsa2.png',dpi=600,bbox_inches='tight')
plt.show()