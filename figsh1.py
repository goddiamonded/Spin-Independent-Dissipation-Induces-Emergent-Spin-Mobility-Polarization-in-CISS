# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:20:10 2026

@author: 83837
"""

import numpy as np
import matplotlib.pyplot as plt
config = {
    "font.family":'Times New Roman',  # font
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

data = np.load('results_lindblad_287.npz', allow_pickle=True)#Gh=0.5meV,G=0.5eV,1/2
data2 = np.load('results_lindblad_539.npz', allow_pickle=True)#Gh=0.5meV,G=0.5eV,1/6
lent=len(data['tlist'])

x=[]
for i in range(0,lent,1):
   x.append(i*27.211*2.419/100/0.12*0.5) 

m1,m2=MSD(data['expect_values'],30,lent)
m5,m6=MSD(data2['expect_values'],30,lent)

plt.plot(x,m1,linewidth=2.0,label='$\\uparrow$,D-localized')
plt.plot(x,m2,'--',linewidth=2.0,label='$\\downarrow$,D-localized')
plt.plot(x,m5,':',linewidth=2.0,label='$\\uparrow$,1/6 spread')
plt.plot(x,m6,'-.',linewidth=2.0,label='$\\downarrow$,1/6 spread')
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(bbox_to_anchor=(0.35,0.77),loc='upper left',frameon=False,prop=font,fontsize=20)

plt.tight_layout()
plt.savefig('figsh1.png',dpi=600,bbox_inches='tight')
plt.show()