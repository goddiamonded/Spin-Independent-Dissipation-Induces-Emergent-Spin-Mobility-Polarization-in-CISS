# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:43:48 2026

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

def fp(f,t=240,dt=100,dt2=80,N=30):
    data = np.load(f, allow_pickle=True)
    lent=len(data['tlist'])
    m1,m2=MSD(data['expect_values'],N,lent)
    return Du(m1,m2,lent,t,dt,dt2)
    
def Du(m1,m2,lent,t,dt,dt2):
   # R=np.zeros((65,65))
    #R1=np.zeros((150,95))
    D=[]
    for i in range(10,200,1):    
        for j in range(i+dt2,200,1):
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
B1=[]  

B1.extend([fp('results_lindblad_313.npz',300,110,110)])
B1.extend([fp('results_lindblad_314.npz',300,120,100)])
B1.extend([fp('results_lindblad_315.npz',300,120,90)])
B1.extend([fp('results_lindblad_281.npz',300,160)])
B1.extend([fp('results_lindblad_458.npz',350,215,72)])
#B1.extend([fp('results_lindblad_316.npz',300,200,70)])
B1.extend([fp('results_lindblad_448.npz',350,210,65)])
#B1.extend([fp('results_lindblad_317.npz',300,210,70)])#GH=3meV
B1.extend([fp('results_lindblad_437.npz',300,200,60)])
#B1.extend([fp('results_lindblad_318.npz',300,200,60)])

B1.extend([fp('results_lindblad_325.npz',300,110,110)])
B1.extend([fp('results_lindblad_324.npz',300,130,110)])#GH=5meV
B1.extend([fp('results_lindblad_323.npz',300,140,100)])
B1.extend([fp('results_lindblad_263.npz',300,150,85)])
B1.extend([fp('results_lindblad_322.npz',300,160,80)])
B1.extend([fp('results_lindblad_321.npz',300,170,70)])
B1.extend([fp('results_lindblad_320.npz',300,170,65)])

cup=[]
for i in range(len(B1)):
    cup.append((B1[i][1]+B1[i][0])/2)

a=[0,1,2,3,4,5,6]

cdown=[]
for i in range(len(B1)):
    cdown.append((B1[i][2]+B1[i][3])/2)
plt.plot(a,cup[0:7],linewidth=3.5,linestyle='solid',marker='o',markersize=8,label='$\\uparrow,\Gamma_H=3meV$')
plt.plot(a,cup[7:14],linewidth=3.5,linestyle='--',marker='s',markersize=8,label='$\\uparrow,\Gamma_H=5meV$') 
plt.plot(a,cdown[0:7],linewidth=3.5,linestyle='-.',marker='*',markersize=8,label='$\\downarrow,\Gamma_H=3meV$')   
plt.plot(a,cdown[7:14],linewidth=3.5,linestyle=':',marker='v',markersize=8,label='$\\downarrow,\Gamma_H=5meV$')

plt.xlabel('$t_{SO}(meV)$',font,fontsize=20)
plt.ylabel('$D_{\\uparrow}$ or $D_{\\downarrow}(fs^{-1})$',font,fontsize=20)
plt.yticks([0.012,0.016,0.02,0.024,0.028],fontsize=20,weight='bold')
plt.xticks(fontsize=20,weight='bold')
plt.legend(frameon=False,bbox_to_anchor=(-0.04,1.08),loc='upper left',prop=font,fontsize=20)
plt.title('right-helix',font,fontsize=20)
plt.tight_layout()
plt.savefig('fig3a.png',dpi=600,bbox_inches='tight')
plt.show()
