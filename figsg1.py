# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 17:42:37 2025

@author: QH
"""
import numpy as np
#import math
import matplotlib.pyplot as plt
from matplotlib import rcParams
config = {
    "font.family":'Times New Roman',  
    "axes.unicode_minus": False 
}
rcParams.update(config)
font={"family":'Times New Roman','weight':'bold','size':20}

data3 = np.load('results_lindblad_312.npz', allow_pickle=True)#G=GH=0
data4 = np.load('results_lindblad_281.npz', allow_pickle=True)#G=0.3eV,GH=3meV
lent=len(data3['tlist'])
b1=data3['expect_values']
b2=data4['expect_values']
i=500
#zi=b1[0:i,2:122:4]+b1[0:i,3:123:4]
#zi2=b1[0:i,3:123:4]
#zi4=b1[0:i,5:125:4]

zi3=b1[4:124:4,0:i]-b1[5:125:4,0:i]

yi=[j for j in range(1,31)]
x=[]
for m in range(int(i)):
    x.append(m*27.211*2.419/100/0.12*0.5)
xi=x

plt.pcolormesh(xi, yi, zi3, vmin=-0.04,vmax=0.04,shading='auto',cmap='bwr')#,vmin=0,vmax=0.02
cbar=plt.colorbar(label='up population')
cbar.set_label("$<\sigma_z(t)>$",fontsize=20)
cbar.ax.tick_params(labelsize=20)
plt.xticks([0,400,800,1200],fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('site number',font,fontsize=20)
plt.tight_layout()
plt.savefig('figsg1a.png',dpi=600,bbox_inches='tight')
plt.show()

zi3=b2[4:124:4,0:i]-b2[5:125:4,0:i]

yi=[j for j in range(1,31)]
x=[]
for m in range(int(i)):
    x.append(m*27.211*2.419/100/0.12*0.5)
xi=x

plt.pcolormesh(xi, yi, zi3, vmin=-0.005,vmax=0.005,shading='auto',cmap='bwr')#,vmin=0,vmax=0.02
cbar=plt.colorbar(label='up population')
cbar.set_label("$<\sigma_z(t)>$",fontsize=20)
cbar.ax.tick_params(labelsize=20)
plt.xticks([0,400,800,1200],fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('site number',font,fontsize=20)
plt.tight_layout()
plt.savefig('figsg1b.png',dpi=600,bbox_inches='tight')
plt.show()

# =============================================================================
# plt.pcolormesh(xi, yi, zi4.T, vmin=0,vmax=0.03,shading='auto',cmap='Blues')#,vmin=0,vmax=0.02
# cbar=plt.colorbar(ticks=[0,0.01,0.02,0.03],label='down population')
# cbar.set_label("down spin population",fontsize=15)
# cbar.ax.tick_params(labelsize=15)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.xlabel('time(fs)',fontsize=15)
# plt.ylabel('n',fontsize=15)
# plt.tight_layout()
# plt.tight_layout()
# #plt.savefig('prl2b.png',dpi=600,bbox_inches='tight')
# plt.show()
# 
# plt.pcolormesh(xi, yi, zi.T,vmin=-0.04,vmax=0.04,shading='auto',cmap='bwr')#,vmin=0,vmax=0.02
# plt.colorbar(label='population')
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.xlabel('time(fs)',fontsize=15)
# plt.ylabel('n',fontsize=15)
# plt.tight_layout()
# #plt.savefig('prl2e.png',dpi=600)
# plt.show()
# 
# plt.pcolormesh(xi, yi, zi2.T, vmin=0,vmax=0.03,shading='auto',cmap='GnBu')#,vmin=0,vmax=0.02
# plt.colorbar(ticks=[0,0.01,0.02,0.03,0.04],label='$\\uparrow$')
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.xlabel('time(fs)',fontsize=15)
# plt.ylabel('n',fontsize=15)
# plt.tight_layout()
# #plt.savefig('prl2f.png',dpi=600)
# plt.show()
# =============================================================================
