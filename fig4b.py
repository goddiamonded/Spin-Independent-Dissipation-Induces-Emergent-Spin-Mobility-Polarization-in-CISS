# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:43:48 2026

@author: 83837
"""
import numpy as np
from loadnpz2c import lr,MSD
import matplotlib.pyplot as plt
config = {
    "font.family":'Times New Roman',  #font 
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
C1=[]

C1.extend([fp('results_lindblad_351.npz',300,160)])
C1.extend([fp('results_lindblad_350.npz',300,160)])
C1.extend([fp('results_lindblad_349.npz',300,160)])
C1.extend([fp('results_lindblad_281.npz',300,160)])#theta=0.66
C1.extend([fp('results_lindblad_348.npz',300,160)])

C1.extend([fp('results_lindblad_352.npz',300,160)])
C1.extend([fp('results_lindblad_353.npz',300,160)])
C1.extend([fp('results_lindblad_354.npz',300,160)])
C1.extend([fp('results_lindblad_355.npz',300,160)])#theta=pi/6
C1.extend([fp('results_lindblad_356.npz',300,160)])

C1.extend([fp('results_lindblad_362.npz',300,140)])
C1.extend([fp('results_lindblad_363.npz',300,140)])
C1.extend([fp('results_lindblad_364.npz',300,140)])
C1.extend([fp('results_lindblad_365.npz',300,140)])#theta=pi/4
C1.extend([fp('results_lindblad_366.npz',300,140)])

C1.extend([fp('results_lindblad_361.npz',300,120,90)])
C1.extend([fp('results_lindblad_360.npz',300,120,90)])
C1.extend([fp('results_lindblad_359.npz',300,120,90)])
C1.extend([fp('results_lindblad_358.npz',300,120,90)])#theta=pi/3
C1.extend([fp('results_lindblad_357.npz',300,120,90)])

C1.extend([fp('results_lindblad_372.npz',300,120,100)])
C1.extend([fp('results_lindblad_371.npz',300,120,100)])
C1.extend([fp('results_lindblad_370.npz',300,120,100)])
C1.extend([fp('results_lindblad_369.npz',300,120,100)])#theta=0.66*2
C1.extend([fp('results_lindblad_367.npz',300,120,100)])

pv=[]

for i in range(25):
    a=(C1[i][0]+C1[i][1])/(C1[i][2]+C1[i][3])
    pv.append((a-1)/(a+1))

x=[1/2,1/3,1/4,1/5,1/6]

plt.plot(x,pv[5:10],linewidth=3.5,markersize=8,linestyle='--',marker='o',label='$\\theta=\\pi/6$')
plt.plot(x,pv[0:5],linewidth=3.5,markersize=8,marker='D',label='$\\theta=0.66$')
plt.plot(x,pv[10:15],linewidth=3.5,markersize=8,linestyle=(0,(1,10)),marker='*',label='$\\theta=\\pi/4$')
plt.plot(x,pv[15:20],linewidth=3.5,markersize=8,linestyle=':',marker='s',label='$\\theta=\\pi/3$')
plt.plot(x,pv[20:25],linewidth=3.5,markersize=8,linestyle='-.',marker='v',label='$\\theta=1.32$')

plt.xlabel('$\\Delta \\varphi(\\pi)$',font,fontsize=20)
plt.ylabel('$P_v$',font,fontsize=20)
#plt.ylim(0.6,2.6)
#plt.xlim(-0.1,6.99)
plt.xticks([0.15,0.2,0.3,0.4,0.5],fontsize=20,weight='bold')
plt.yticks([0.1,0.15,0.2,0.25,0.3],fontsize=20,weight='bold')
plt.legend(ncol=2,prop=font,bbox_to_anchor=(1.03,0.24),fontsize=20,loc='right',frameon=False)
plt.tight_layout()
plt.savefig('fig4a.png',dpi=600,bbox_inches='tight')
plt.show()
  