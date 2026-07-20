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
C2=[]

C2.extend([fp('results_lindblad_501.npz',50,15,15,50,N=1)])
C2.extend([fp('results_lindblad_347.npz',60,17,31,100,N=5)])
C2.extend([fp('results_lindblad_334.npz',200,87,40,100,N=10)])
C2.extend([fp('results_lindblad_333.npz',300,105,55,190,N=15)])
C2.extend([fp('results_lindblad_332.npz',300,125,65,N=20)])
C2.extend([fp('results_lindblad_331.npz',300,160,70,N=25)])
C2.extend([fp('results_lindblad_281.npz',300,160)])#0.66
#C2.extend([fp('results_lindblad_330.npz',300,160,90,N=35)])

C2.extend([fp('results_lindblad_492.npz',50,15,15,50,N=1)])
C2.extend([fp('results_lindblad_491.npz',100,31,17,60,N=5)])
C2.extend([fp('results_lindblad_490.npz',100,40,87,200,N=10)])
C2.extend([fp('results_lindblad_489.npz',190,55,105,300,N=15)])
C2.extend([fp('results_lindblad_488.npz',200,65,125,300,N=20)])
C2.extend([fp('results_lindblad_487.npz',200,70,160,300,N=25)])
C2.extend([fp('results_lindblad_411.npz',200,80,160,300)])#0.66,left

C2.extend([fp('results_lindblad_493.npz',50,15,15,50,N=1)])
C2.extend([fp('results_lindblad_376.npz',100,20,33,100,N=5)])
C2.extend([fp('results_lindblad_377.npz',175,75,52,150,N=10)])
C2.extend([fp('results_lindblad_378.npz',200,73,70,150,N=15)])
C2.extend([fp('results_lindblad_379.npz',200,100,80,150,N=20)])
C2.extend([fp('results_lindblad_380.npz',250,120,90,150,N=25)])
C2.extend([fp('results_lindblad_358.npz',300,125,95)])#pi/3

C2.extend([fp('results_lindblad_500.npz',50,15,15,50,N=1)])
C2.extend([fp('results_lindblad_494.npz',100,33,20,100,N=5)])
C2.extend([fp('results_lindblad_495.npz',150,52,75,175,N=10)])
C2.extend([fp('results_lindblad_496.npz',150,70,73,200,N=15)])
C2.extend([fp('results_lindblad_497.npz',150,80,100,200,N=20)])
C2.extend([fp('results_lindblad_498.npz',150,90,120,250,N=25)])
C2.extend([fp('results_lindblad_499.npz',200,95,125,300)])#pi/3,left

C2.extend([fp('results_lindblad_502.npz',50,15,15,50,N=1)])#pi/2
C2.extend([fp('results_lindblad_503.npz',100,30,30,100,N=5)])
C2.extend([fp('results_lindblad_504.npz',150,90,90,150,N=10)])#pi/2
C2.extend([fp('results_lindblad_505.npz',200,80,80,200,N=15)])
C2.extend([fp('results_lindblad_506.npz',200,100,100,200,N=20)])#pi/2
C2.extend([fp('results_lindblad_507.npz',250,100,100,250,N=25)])
C2.extend([fp('results_lindblad_508.npz',250,110,110,250,N=30)])#pi/2

font1={"family":'Times New Roman','weight':'bold','size':18}
pv=[]
for i in range(35):
    a=(C2[i][0]+C2[i][1])/(C2[i][2]+C2[i][3])
    pv.append((a-1)/(a+1))   

pol=pv[0:7]
pol2=pv[7:14]
pol3=pv[14:21]
pol4=pv[21:28]
pol5=pv[28:35]
x=[1,5,10,15,20,25,30]

plt.plot(x,pol,linewidth=3.5,markersize=8,linestyle='--',marker='o',label='right,$\\theta=0.66$')
plt.plot(x,pol3,linewidth=3.5,markersize=8,marker='D',label='right,$\\theta=\\pi/3$')
plt.plot(x,pol5,linewidth=3.5,markersize=8,linestyle=(0,(1,10)),marker='*',label='$\Delta\\varphi=0,\\theta=\\pi/2$')
plt.plot(x,pol4,linewidth=3.5,markersize=8,linestyle='-.',marker='v',label='left,$\\theta=2\\pi/3$')
plt.plot(x,pol2,linewidth=3.5,markersize=8,linestyle=':',marker='s',label='left,$\\theta=\pi-0.66$')


plt.xlabel('length N',font,fontsize=20)
plt.ylabel('$P_v$',font,fontsize=20)
#plt.ylim(0.6,2.6)
#plt.xlim(-0.1,6.99)
plt.xticks(fontsize=20,weight='bold')
plt.yticks(fontsize=20,weight='bold')
plt.legend(fontsize=20,bbox_to_anchor=(1.03,0.58),prop=font1,loc='right',frameon=False)
plt.tight_layout()
plt.savefig('fig4b.png',dpi=600,bbox_inches='tight')
plt.show()