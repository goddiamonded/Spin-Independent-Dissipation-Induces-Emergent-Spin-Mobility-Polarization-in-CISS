# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:43:48 2026

@author: 83837
"""
import numpy as np
from loadnpz2c import lr,MSD
from fig3a import B1
from fig3b import B2
import matplotlib.pyplot as plt
config = {
    "font.family":'Times New Roman',  # font
    "axes.unicode_minus": False 
}
from matplotlib import rcParams
rcParams.update(config)
font={"family":'Times New Roman','weight':'bold','size':18}

def fp(f,t=240,dt=100,dt2=80,t2=200,N=30):
    data = np.load(f, allow_pickle=True)
    lent=len(data['tlist'])
    m1,m2=MSD(data['expect_values'],N,lent)
    return Du(m1,m2,lent,t,dt,dt2,t2)

def Du(m1,m2,lent,t,dt,dt2,t2):
   # R=np.zeros((65,65))
    #R1=np.zeros((150,95))
    D=[]
    for i in range(10,t,1):    
        for j in range(i+dt,t,1):
            r,r1,r2,r3=lr(m1,m2,i,j,48,71,lent)
            #R[i-15,j-40]=r
            if r>0.999:               
                D.append(r2)
    print(min(D),max(D))            
    D1=[]
    for i in range(10,t2-dt2,1): #20,170 for N=5   
        for j in range(i+dt2,t2,1):  #60, 210 FOR n=5
            r,r1,r2,r3=lr(m1,m2,29,48,i,j,lent)
            #R1[i-30,j-55]=r1
            if r1>0.999:
                D1.append(r3)
    print(min(D1),max(D1))            
    return min(D),max(D),min(D1),max(D1)

pvr=[]
pvl=[]
for i in range(len(B2)):
    a=(B1[i][1]+B1[i][0])/(B1[i][2]+B1[i][3])
    b=(B2[i][1]+B2[i][0])/(B2[i][2]+B2[i][3])
    pvr.append((a-1)/(a+1))
    pvl.append((b-1)/(b+1))
a=[0,1,2,3,4,5,6]

plt.plot(a,pvr[0:7],linewidth=3.5,linestyle='solid',markersize=8,marker='o',label='right,$\Gamma_H=3meV$')
plt.plot(a,pvr[7:14],linewidth=3.5,linestyle='--',markersize=8,marker='s',label='right,$\Gamma_H=5meV$') 
plt.plot(a,pvl[0:7],linewidth=3.5,linestyle='-.',markersize=8,marker='*',label='left,$\Gamma_H=3meV$')   
plt.plot(a,pvl[7:14],linewidth=3.5,linestyle=':',markersize=8,marker='v',label='left,$\Gamma_H=5meV$')

plt.xlabel('$t_{SO}(meV)$',font,fontsize=20)
plt.ylabel('$P_v$',font,fontsize=20)
plt.yticks(fontsize=20,weight='bold')
plt.xticks(fontsize=20,weight='bold')
font1={"family":'Times New Roman','weight':'bold','size':19}
plt.legend(frameon=False,bbox_to_anchor=(1.05,0.5),loc='center right',prop=font1,fontsize=20)
plt.tight_layout()
plt.savefig('fig3c.png',dpi=600,bbox_inches='tight')
plt.show()