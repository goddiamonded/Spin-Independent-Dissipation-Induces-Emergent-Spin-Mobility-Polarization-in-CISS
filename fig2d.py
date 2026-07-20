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
    for i in range(30,200,1):    
        for j in range(i+dt2,200,1):
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
A1=[]  
#A.extend([fp('results_lindblad_255.npz')])
A1.extend([fp('results_lindblad_287.npz',400,300,95)])#GH=0.6meV
#A1.extend([fp('results_lindblad_288.npz',400,300,90)])

A1.extend([fp('results_lindblad_292.npz',400,260,95)])#GH=0.8meV
#A1.extend([fp('results_lindblad_291.npz',400,250,90)])

A1.extend([fp('results_lindblad_165.npz',400,230,95)])#GH=1meV

A1.extend([fp('results_lindblad_294.npz',400,150,85)])#GH=2meV

A1.extend([fp('results_lindblad_281.npz',300,160)])#GH=3meV

A1.extend([fp('results_lindblad_297.npz',300,150,80)])#GH=4meV

A1.extend([fp('results_lindblad_263.npz',300,150,85)])#GH=5meV

A1.extend([fp('results_lindblad_299.npz',250,150,90)])#GH=6mev
#A1.extend([fp('results_lindblad_300.npz',250,150,90)])

A1.extend([fp('results_lindblad_302.npz',240,150,90)])#GH=7mev

A1.extend([fp('results_lindblad_303.npz',240,150,100)])#GH=8mev

pv=[]
for i in range(len(A1)):
    a=(A1[i][1]+A1[i][0])/(A1[i][2]+A1[i][3])
    pv.append((a-1)/(a+1))
charge=[]
for i in range(len(A1)):
    a=(A1[i][1]+A1[i][0]+A1[i][2]+A1[i][3])/2
    charge.append(a)    
a=[0.6,0.8,1,2,3,4,5,6,7,8]  
         
fig, ax1 = plt.subplots()  
ax2 = ax1.twinx()
line1 = ax1.plot(a,pv,color='blue',linewidth=3.5,linestyle='solid',marker='o',markersize=8,label='$P_v$')
line2 = ax2.plot(a,charge,color='red',linewidth=3.5,linestyle='--',marker='s',markersize=8,label='$D_{\\uparrow}+D_{\\downarrow}$')
ax1.set_xlabel('$\Gamma_H(meV)$', font,fontsize=20)  
ax1.set_ylabel('$P_v$',font,fontsize=20)  
ax2.set_ylabel('$D_{\\uparrow}+D_{\\downarrow}(fs^{-1})$',font,fontsize=20)
ax1.set_yticks([0.1,0.2,0.3,0.4,0.5])
ax1.set_yticklabels(['0.1','0.2','0.3','0.4','0.5'],fontsize=20,weight='bold')
ax2.set_yticks([0.03,0.032,0.034,0.036,0.038])
ax2.set_yticklabels(['0.03','0.032','0.034','0.036','0.038'],fontsize=20,weight='bold')
ax1.set_xticks([0,2,4,6,8])
ax1.set_xticklabels(['0','2','4','6','8'],fontsize=20,weight='bold')

ax1.tick_params('y', colors='blue')  
ax2.tick_params('y', colors='red')  
#设置轴颜色  
ax1.spines['left'].set_color('blue')  
ax2.spines['left'].set_color('blue')  
ax1.spines['right'].set_color('red')  
ax2.spines['right'].set_color('red')
lines = line1 + line2  
labels = [h.get_label() for h in lines] 
font1={"family":'Times New Roman','weight':'bold','size':23} 
plt.legend(lines, labels, loc='upper right',frameon=False,fontsize=23,prop=font1)
#plt.legend(fontsize=16)
plt.tight_layout()
plt.savefig('fig2d.png',dpi=600,bbox_inches='tight')
plt.show()
