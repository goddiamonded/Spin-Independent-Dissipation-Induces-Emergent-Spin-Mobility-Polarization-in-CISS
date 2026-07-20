# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:20:10 2026

@author: 83837
"""

import numpy as np
from loadnpz2c import lr,MSD
import matplotlib.pyplot as plt
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
    for i in range(30,t2,1):    
        for j in range(i+dt2,t2,1):
            r,r1,r2,r3=lr(m1,m2,i,j,48,71,lent)
            #R[i-15,j-40]=r
            if r>0.999:               
                D.append(r2)
    print(min(D),max(D))            
    D1=[]
    for i in range(30,t-dt,1): #20,170 for N=5   
        for j in range(i+dt,t,1):  #60, 210 FOR n=5
            r,r1,r2,r3=lr(m1,m2,29,48,i,j,lent)
            #R1[i-30,j-55]=r1
            if r1>0.999:
                D1.append(r3)
    print(min(D1),max(D1))            
    return min(D),max(D),min(D1),max(D1)

H1=[]  
H1.extend([fp('results_lindblad_396.npz',300,180,210,300)])#epi_D=0.458eV
H1.extend([fp('results_lindblad_402.npz',300,180,210,300)])#epi_D=0.46eV
H1.extend([fp('results_lindblad_559.npz',300,190,160,300)])#epi_D=0.462eV
H1.extend([fp('results_lindblad_558.npz',300,220,120,250)])#epi_D=0.464eV
H1.extend([fp('results_lindblad_557.npz',300,220,90,250)])#epi_D=0.466eV
H1.extend([fp('results_lindblad_281.npz',300,160)])#epi_D=0.468eV
H1.extend([fp('results_lindblad_401.npz',300,130,75,200)])#epi_D=0.47eV
H1.extend([fp('results_lindblad_556.npz',300,110,70,200)])#epi_D=0.472eV
H1.extend([fp('results_lindblad_555.npz',250,100,65,200)])#epi_D=0.474eV
H1.extend([fp('results_lindblad_554.npz',250,95,65,150)])#epi_D=0.476eV
H1.extend([fp('results_lindblad_395.npz',250,90,60,150)])#epi_D=0.478eV
H1.extend([fp('results_lindblad_553.npz',250,80,55,150)])#epi_D=0.48eV
H1.extend([fp('results_lindblad_568.npz',200,60,42,150)])#epi_D=0.49eV
H1.extend([fp('results_lindblad_552.npz',150,45,37,130)])#epi_D=0.5eV
#H1.extend([fp('results_lindblad_551.npz',120,37,35,120)])#epi_D=0.55eV

pv=[]
error=[]
for i in range(len(H1)):
    a=(H1[i][1]+H1[i][0])/(H1[i][2]+H1[i][3])
    error.append((H1[i][1]/H1[i][2]-H1[i][0]/H1[i][3])/2)
    pv.append((a-1)/(a+1))  
a=[0.458,0.46,0.462,0.464,0.466,0.468,0.47,0.472,0.474,0.476,0.478,0.48,0.49,0.5]
plt.errorbar(a,pv,error,linewidth=2.0,linestyle='solid',marker='o',markersize=6,label='$\\uparrow$,D-localized')
plt.xlabel('$\\epsilon_D(eV)$',font,fontsize=20)
plt.ylabel('$P_v$',font,fontsize=20)
plt.xticks(fontsize=20)#[0.458,0.462,0.466,0.47,0.474,0.478,0.482],
plt.yticks(fontsize=20)

plt.tight_layout()
#plt.savefig('figsh2.png',dpi=600,bbox_inches='tight')
plt.show()