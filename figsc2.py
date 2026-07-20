# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:02:46 2026

@author: 83837
"""
import matplotlib.pyplot as plt
from loadnpz2c import lr,MSD
import numpy as np
config = {
    "font.family":'Times New Roman',  # 
    "axes.unicode_minus": False 
}
from matplotlib import rcParams
rcParams.update(config)
font={"family":'Times New Roman','weight':'bold','size':20}

def fp(f,t=240,dt=100,dt2=80,t2=200,N=30):
    data = np.load(f, allow_pickle=True)
    lent=len(data['tlist'])
    m1,m2=MSD(data['expect_values'],N,lent)
    return Du(m1,m2,lent,t,dt,dt2,t2)
    
def Du(m1,m2,lent,t,dt,dt2,t2):
   # R=np.zeros((65,65))
    #R1=np.zeros((150,95))
    D=[]
    for i in range(10,t2,1):    
        for j in range(i+dt2,t2,1):
            r,r1,r2,r3=lr(m1,m2,i,j,48,71,lent)
            #R[i-15,j-40]=r
            if r>0.999:               
                D.append(r2)
    print(min(D),max(D))            
    D1=[]
    for i in range(10,t-dt,1): #20,170 for N=5   
        for j in range(i+dt,t,1):  #60, 210 FOR n=5
            r,r1,r2,r3=lr(m1,m2,29,48,i,j,lent)
            #R1[i-30,j-55]=r1
            if r1>0.999:
                D1.append(r3)
    print(min(D1),max(D1))            
    return min(D),max(D),min(D1),max(D1)

A5=[] #GH=0
A5.extend([fp('results_lindblad_113.npz',350,180,95)])#0.3
A5.extend([fp('results_lindblad_232.npz',350,190,100)])#0.4
A5.extend([fp('results_lindblad_114.npz',350,200,100)])#0.5
A5.extend([fp('results_lindblad_233.npz',350,210,105)])#0.6
A5.extend([fp('results_lindblad_115.npz',350,220,105)])#0.7
A5.extend([fp('results_lindblad_234.npz',350,220,105)])#0.8
A5.extend([fp('results_lindblad_116.npz',350,220,105)])#0.9
A5.extend([fp('results_lindblad_117.npz',350,220,110)])#1
A5.extend([fp('results_lindblad_118.npz',350,220,110)])#1.1
A5.extend([fp('results_lindblad_119.npz',350,210,110)])#1.3

Dupmax=[]
Dupmin=[]
Ddomax=[]
Ddomin=[]
for i in range(len(A5)):
    Dupmax.append(A5[i][1])
    Dupmin.append(A5[i][0])
    Ddomax.append(A5[i][3])
    Ddomin.append(A5[i][2])

pv=[]
error=[]
for i in range(10):
    a=(Dupmax[i]+Dupmin[i])/(Ddomax[i]+Ddomin[i])
    b=Dupmax[i]/Ddomin[i]
    c=(Dupmin[i])/(Ddomax[i])
    pv.append((a-1)/(a+1))
    error.append((b-1)/(b+1)/2-(c-1)/(c+1)/2)
a=[0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,(1.3)]
#plt.xscale('log')
#plt.yscale('log')
plt.errorbar(a,pv,error,fmt='o', capsize=3, 
              alpha=0.6,linewidth=2.0,linestyle='solid',label='$P_v$')

plt.yticks([0.445,0.455,0.465,0.475,0.485],fontsize=20)
#plt.xlim(0.29,1.55)
plt.xticks(fontsize=20)
#plt.legend(frameon=False,fontsize=15)
#plt.ylim(0.02,0.06)
plt.grid(True, which='both', linestyle='--', linewidth=2.0,alpha=0.5)
plt.xlabel('$\Gamma(eV)$',font,fontsize=20)
plt.ylabel('$P_v$',font,fontsize=20)
plt.legend(frameon=False,prop=font,fontsize=20)
plt.tight_layout()
#plt.savefig('figsb2.png',dpi=600,bbox_inches='tight')
plt.show()