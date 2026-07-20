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
B4=[]  

B4.extend([fp('results_lindblad_432.npz',300,110,110)])#tso=0
B4.extend([fp('results_lindblad_432.npz',300,110,110)])#tso=0
B4.extend([fp('results_lindblad_432.npz',300,110,110)])#tso=0
B4.extend([fp('results_lindblad_432.npz',300,110,110)])#tso=0
B4.extend([fp('results_lindblad_432.npz',300,110,110)])#tso=0

B4.extend([fp('results_lindblad_479.npz',400,150,105,200)])
B4.extend([fp('results_lindblad_480.npz',350,120,105,200)])#tso=1meV
B4.extend([fp('results_lindblad_481.npz',300,120,100)])
B4.extend([fp('results_lindblad_482.npz',350,120,100,200)])
B4.extend([fp('results_lindblad_483.npz',350,120,105,300)])

B4.extend([fp('results_lindblad_475.npz',400,100,95,200)])
B4.extend([fp('results_lindblad_476.npz',350,135,95,200)])#tso=2meV
B4.extend([fp('results_lindblad_477.npz',300,120,90)])
B4.extend([fp('results_lindblad_478.npz',350,130,85,200)])
B4.extend([fp('results_lindblad_472.npz',350,140,100,300)])

B4.extend([fp('results_lindblad_464.npz',400,150,85,200)])
B4.extend([fp('results_lindblad_465.npz',350,160,85,200)])#tso=3meV
B4.extend([fp('results_lindblad_281.npz',300,160)])
B4.extend([fp('results_lindblad_466.npz',350,170,85,200)])
B4.extend([fp('results_lindblad_468.npz',350,175,200,400)])

B4.extend([fp('results_lindblad_454.npz',600,450,75,200)])
B4.extend([fp('results_lindblad_456.npz',350,210,75,200)])#tso=4meV
B4.extend([fp('results_lindblad_458.npz',350,215,72,200)])
B4.extend([fp('results_lindblad_459.npz',350,220,70,200)])
B4.extend([fp('results_lindblad_462.npz',350,230,300,600)])

B4.extend([fp('results_lindblad_445.npz',600,450,65,200)])
B4.extend([fp('results_lindblad_446.npz',350,200,65,200)])#tso=5meV
B4.extend([fp('results_lindblad_448.npz',350,210,65,200)])
B4.extend([fp('results_lindblad_451.npz',350,220,65,200)])
B4.extend([fp('results_lindblad_452.npz',350,230,300,600)])

B4.extend([fp('results_lindblad_428.npz',200,65,550,600)])
B4.extend([fp('results_lindblad_440.npz',350,210,60,200)])#tso=6meV
B4.extend([fp('results_lindblad_437.npz',300,200,60,200)])
B4.extend([fp('results_lindblad_443.npz',350,210,60,200)])
B4.extend([fp('results_lindblad_434.npz',500,270,200,300)])

lin1=[]
lin2=[]
lin3=[]
lin4=[]
lin5=[]
for i in range(35):
    if i%5==0:
        lin1.append((B4[i][1]+B4[i][0]+B4[i][2]+B4[i][3])/2)
    if i%5==1:
        lin2.append((B4[i][1]+B4[i][0]+B4[i][2]+B4[i][3])/2)
    if i%5==2:
        lin3.append((B4[i][1]+B4[i][0]+B4[i][2]+B4[i][3])/2)
    if i%5==3:
        lin4.append((B4[i][1]+B4[i][0]+B4[i][2]+B4[i][3])/2)
    if i%5==4:
        lin5.append((B4[i][1]+B4[i][0]+B4[i][2]+B4[i][3])/2)

font1={"family":'Times New Roman','weight':'bold','size':16.5}
x=[0,1,2,3,4,5,6]    
plt.plot(x,lin1,marker='D',linewidth=3.5,markersize=8,label='100%$\\uparrow$')
plt.plot(x,lin2,linestyle='--',linewidth=3.5,marker='o',markersize=8,label='75%$\\uparrow$25%$\\downarrow$')
plt.plot(x,lin3,linestyle='-.',linewidth=3.5,marker='v',markersize=8,label='50%$\\uparrow$50%$\\downarrow$')
plt.plot(x,lin4,linestyle=':',linewidth=3.5,marker='s',markersize=8,label='25%$\\uparrow$75%$\\downarrow$')
plt.plot(x,lin5,linestyle=(0,(1,10)),linewidth=3.5,marker='*',markersize=8,label='100%$\\downarrow$')
plt.xlabel('$t_{SO}(meV)$',font,fontsize=20)
plt.ylabel('$D_{\\uparrow}+D_{\\downarrow}(fs^{-1})$',font,fontsize=20)
plt.ylim(0.021,0.059)
#plt.xlim(-0.1,6.99)
plt.xticks(fontsize=20,weight='bold')
plt.yticks(fontsize=20,weight='bold')
plt.legend(ncol=2,bbox_to_anchor=(-0.045,1.05),loc=2,prop=font1,fontsize=17,frameon=False)
plt.tight_layout()
plt.savefig('fig3d.png',dpi=600,bbox_inches='tight')
plt.show()