# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:49:06 2026

@author: 83837
"""

import numpy as np
import matplotlib.pyplot as plt
config = {
    "font.family":'Times New Roman',  
    "axes.unicode_minus": False 
}
from matplotlib import rcParams
rcParams.update(config)
font={"family":'Times New Roman','weight':'bold','size':20}

Gup=[]
Gdown=[]
data3 = np.load('results_lindblad_312.npz', allow_pickle=True)#G=GH=0
lent=len(data3['tlist'])
for j in range(lent):
    a=0
    b=0
    for i in range(30*2+2):
       a+=data3['expect_values'][2*i][j] 
       b+=data3['expect_values'][2*i+1][j]
    Gup.append(a)
    Gdown.append(b) 
    if len(Gup)%400==0:
        print(len(Gup))
    
Gup1=[]
Gdown1=[]
data4 = np.load('results_lindblad_281.npz', allow_pickle=True)#G=0.3eV,GH=3meV
lent=len(data4['tlist'])
for j in range(lent):
    a=0
    b=0
    for i in range(30*2+2):
       a+=data4['expect_values'][2*i][j] 
       b+=data4['expect_values'][2*i+1][j]
    Gup1.append(a)
    Gdown1.append(b)
    if len(Gup1)%400==0:
        print(len(Gup1))

x=[]
for m in range(lent):
    x.append(m*27.211*2.419/100/0.12*0.5)

fig, ax = plt.subplots(figsize=(6, 4))
line1,=ax.plot(x,Gup,linestyle='solid',linewidth=2.0,label='$\\uparrow$,purely electronic')
line2,=ax.plot(x,Gdown,linestyle=':',linewidth=2.0,label='$\\downarrow$,purely electronic')
line3,=ax.plot(x,Gup1,linestyle='--',linewidth=2.0,label='$\\uparrow,\\Gamma=0.3eV,\\Gamma_H=3meV$')
line4,=ax.plot(x,Gdown1,linestyle='-.',linewidth=2.0,label='$\\downarrow,\\Gamma=0.3eV,\\Gamma_H=3meV$')

first_legend = ax.legend(handles=[line1, line2], loc='upper left',frameon=False,prop=font,fontsize=20)
ax.add_artist(first_legend)
ax.legend(handles=[line3, line4], loc='lower right',frameon=False,prop=font,fontsize=20)

plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('total population',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(0.495,0.505)
#plt.legend(frameon=False,prop=font,fontsize=20)

plt.tight_layout()
plt.savefig('figsf1.png',dpi=600,bbox_inches='tight')
plt.show()