# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:02:46 2026

@author: 83837
"""
import matplotlib.pyplot as plt
from loadnpz2c import lr,MSD
import numpy as np
config = {
    "font.family":'Times New Roman',  # font
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

A1=[]
A1.extend([fp('results_lindblad_113.npz',400,200,95)])#GH=0meV
A1.extend([fp('results_lindblad_388.npz',400,220,95)])#GH=0.1meV
A1.extend([fp('results_lindblad_386.npz',400,260,95)])#GH=0.2meV
A1.extend([fp('results_lindblad_389.npz',400,330,95)])#GH=0.3meV
A1.extend([fp('results_lindblad_387.npz',400,330,90)])#Gh=0.4meV

Dupmax=[]
Dupmin=[]
Ddomax=[]
Ddomin=[]
for i in range(len(A1)):
    Dupmax.append(A1[i][1])
    Dupmin.append(A1[i][0])
    Ddomax.append(A1[i][3])
    Ddomin.append(A1[i][2])

pv=[]
error=[]
for i in range(len(A1)):
    a=(Dupmax[i]+Dupmin[i])/(Ddomax[i]+Ddomin[i])
    b=Dupmax[i]/Ddomin[i]
    c=(Dupmin[i])/(Ddomax[i])
    pv.append((a-1)/(a+1))
    error.append((b-1)/(b+1)/2-(c-1)/(c+1)/2)
a=[0,0.1,0.2,0.3,0.4]
#plt.xscale('log')
#plt.yscale('log')
plt.plot(a,pv,linestyle='solid',marker='o',linewidth=2.0,label='$\Gamma=0.3eV$')

plt.yticks([0.475,0.48,0.485,0.49,0.495,0.5],fontsize=20)
#plt.xlim(0,0.44)
plt.xticks([0,0.1,0.1,0.2,0.3,0.4],fontsize=20)
#plt.legend(frameon=False,fontsize=15)
#plt.ylim(0.02,0.06)
plt.xlabel('$\Gamma_H(meV)$',font,fontsize=20)
plt.ylabel('$P_v$',font,fontsize=20)
plt.legend(frameon=False,prop=font,fontsize=20)
plt.tight_layout()
plt.savefig('fig2s3.png',dpi=600,bbox_inches='tight')
plt.show()