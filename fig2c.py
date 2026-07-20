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
    D1=[]
    for i in range(30,t-dt,1): #20,170 for N=5   
        for j in range(i+dt,t,1):  #60, 210 FOR n=5
            r,r1,r2,r3=lr(m1,m2,29,48,i,j,lent)
            #R1[i-30,j-55]=r1
            if r1>0.999:
                D1.append(r3)
    print(min(D),max(D),min(D1),max(D1))            
    return min(D),max(D),min(D1),max(D1)
A=[]  #GH=0.005
#A.extend([fp('results_lindblad_255.npz')])
A.extend([fp('results_lindblad_261.npz',dt=140)])
A.extend([fp('results_lindblad_262.npz',dt=140)])
A.extend([fp('results_lindblad_235.npz',dt=140)])
A.extend([fp('results_lindblad_263.npz',dt=140)])
A.extend([fp('results_lindblad_236.npz',dt=140)])
A.extend([fp('results_lindblad_237.npz',dt=140)])
A.extend([fp('results_lindblad_238.npz',dt=140)])
A.extend([fp('results_lindblad_239.npz',dt=140)])
A.extend([fp('results_lindblad_240.npz',dt=140)])
A.extend([fp('results_lindblad_241.npz',dt=130)])
A.extend([fp('results_lindblad_243.npz',dt=120)])
A2=[] #GH=0.01
#A2.extend([fp('results_lindblad_264.npz')])
A2.extend([fp('results_lindblad_265.npz',dt=120,dt2=100)])
A2.extend([fp('results_lindblad_266.npz',dt=130,dt2=110)])
A2.extend([fp('results_lindblad_245.npz',dt=130,dt2=110)])
A2.extend([fp('results_lindblad_274.npz',dt=130,dt2=110)])
A2.extend([fp('results_lindblad_246.npz',dt=130,dt2=110)])
A2.extend([fp('results_lindblad_247.npz',dt=130,dt2=110)])
A2.extend([fp('results_lindblad_248.npz',dt=130,dt2=100)])
A2.extend([fp('results_lindblad_249.npz',dt=130,dt2=100)])
A2.extend([fp('results_lindblad_250.npz',dt=130,dt2=100)])
A2.extend([fp('results_lindblad_251.npz',dt=130,dt2=100)])
A2.extend([fp('results_lindblad_253.npz',dt=130,dt2=90)])
A3=[] #GH=0.001
A3.extend([fp('results_lindblad_270.npz',400,300,55)])
A3.extend([fp('results_lindblad_269.npz',400,305,60)])
A3.extend([fp('results_lindblad_167.npz',400,305,70)])
A3.extend([fp('results_lindblad_272.npz',400,295,75)])
A3.extend([fp('results_lindblad_268.npz',400,285,80)])
A3.extend([fp('results_lindblad_166.npz',400,255,87)])
A3.extend([fp('results_lindblad_267.npz',400,240,90)])
A3.extend([fp('results_lindblad_165.npz',400,230,90)])
A3.extend([fp('results_lindblad_273.npz',400,225,90)])
A3.extend([fp('results_lindblad_164.npz',400,230,95)])
A3.extend([fp('results_lindblad_162.npz',400,235,95)])
A4=[] #GH=0.003
A4.extend([fp('results_lindblad_276.npz',300,145,70)])
A4.extend([fp('results_lindblad_277.npz',300,150,70)])
A4.extend([fp('results_lindblad_278.npz',300,165,70)])
A4.extend([fp('results_lindblad_279.npz',300,165,80)])
A4.extend([fp('results_lindblad_280.npz',300,165)])
A4.extend([fp('results_lindblad_281.npz',300,165)])
A4.extend([fp('results_lindblad_282.npz',300,150)])
A4.extend([fp('results_lindblad_283.npz',300,150)])
A4.extend([fp('results_lindblad_284.npz',300,140)])
A4.extend([fp('results_lindblad_285.npz',300,140)])
A4.extend([fp('results_lindblad_286.npz',300,130)])
'''
A5=[] #GH=0
A5.extend([fp('results_lindblad_113.npz',350,180,95)])
A5.extend([fp('results_lindblad_232.npz',350,190,100)])
A5.extend([fp('results_lindblad_114.npz',350,200,100)])
A5.extend([fp('results_lindblad_233.npz',350,210,105)])
A5.extend([fp('results_lindblad_115.npz',350,220,105)])
A5.extend([fp('results_lindblad_234.npz',350,220,105)])
A5.extend([fp('results_lindblad_116.npz',350,220,105)])
A5.extend([fp('results_lindblad_117.npz',350,220,110)])
A5.extend([fp('results_lindblad_118.npz',350,220,110)])
A5.extend([fp('results_lindblad_119.npz',350,210,110)])
#A5.extend([fp('results_lindblad_120.npz',350,210,110)])
'''

Dupmax=[]
Dupmin=[]
Ddomax=[]
Ddomin=[]
for i in range(len(A)):
    Dupmax.append(A[i][1])
    Dupmin.append(A[i][0])
    Ddomax.append(A[i][3])
    Ddomin.append(A[i][2])
for i in range(len(A)):
    Dupmax.append(A2[i][1])
    Dupmin.append(A2[i][0])
    Ddomax.append(A2[i][3])
    Ddomin.append(A2[i][2])  
for i in range(len(A)):
    Dupmax.append(A3[i][1])
    Dupmin.append(A3[i][0])
    Ddomax.append(A3[i][3])
    Ddomin.append(A3[i][2])      
for i in range(len(A4)):
    Dupmax.append(A4[i][1])
    Dupmin.append(A4[i][0])
    Ddomax.append(A4[i][3])
    Ddomin.append(A4[i][2])

De=[]
error=[]
for i in range(0,44,1):
    De.append((Dupmax[i]+Dupmin[i]+Ddomax[i]+Ddomin[i])/2)
    error.append((Dupmax[i]+Ddomax[i]-Dupmin[i]-Ddomin[i])/2)    
a=[0.06,0.08,0.1,0.15,0.2,0.3,0.4,0.5,0.6,(0.7),(0.9)]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(a[0:11],De[22:33],linewidth=3.0,linestyle='solid',marker='v',label='$\Gamma_H=1meV$',markersize=8)
ax.plot(a,De[33:44],linewidth=3.0,linestyle='-.',marker='o',label='$\Gamma_H=3meV$',markersize=8)
ax.plot(a,De[0:11],linewidth=3.0,linestyle='--',marker='s',label='$\Gamma_H=5meV$',markersize=8)
ax.plot(a,De[11:22],linewidth=3.0,linestyle=':',marker='*',label='$\Gamma_H=10meV$',markersize=8)
ax.grid(True, which='both', linestyle='--', linewidth=3.0,alpha=0.5)
ax.set_yscale('log')
ax.set_yticks([0.02,0.03,0.04,0.06])
ax.set_yticklabels(['0.02', '0.03', '0.04', '0.06'], fontsize=20,weight='bold')
ax.set_xscale('log')
ax.set_xticks([0.06,0.1,0.2,0.5,1])
ax.set_xticklabels(['0.06', '0.1', '0.2', '0.5', '1'], fontsize=20,weight='bold')

ax.legend(ncol=2,bbox_to_anchor=(-0.04, 0.8),loc=6,frameon=False,fontsize=17.5)
#plt.ylim(0.02,0.08)
ax.set_xlabel('$\Gamma(eV)$',font,fontsize=20)
ax.set_ylabel('$D_{\\uparrow}+D_{\\downarrow}(fs^{-1})$',font,fontsize=20)

plt.tight_layout()
plt.savefig('fig2c.png',dpi=600,bbox_inches='tight')
plt.show()
  