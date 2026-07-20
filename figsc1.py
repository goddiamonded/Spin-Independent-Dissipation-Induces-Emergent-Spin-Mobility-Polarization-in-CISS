# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:43:48 2026

@author: 83837
"""
import numpy as np
from loadnpz2c import lr,MSD
import matplotlib.pyplot as plt

config = {
    "font.family":'Times New Roman',  
    "axes.unicode_minus": False 
}
from matplotlib import rcParams
rcParams.update(config)
font={"family":'Times New Roman','weight':'bold','size':20}


data4 = np.load('results_lindblad_112.npz', allow_pickle=True)#G=0.1,GH=0
lent=len(data4['tlist'])
x=[]
for m in range(lent):
    x.append(m*27.211*2.419/100/0.12*0.5)

m7,m8=MSD(data4['expect_values'],30,lent)
plt.plot(x,m7,linewidth=2.0,label='$\\uparrow$')
plt.plot(x,m8,':',linewidth=2.0,label='$\\downarrow$')
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(ncol=2,fontsize=20,prop=font,frameon=False)

plt.tight_layout()
plt.savefig('figsc1b.png',dpi=600,bbox_inches='tight')
plt.show()

data4 = np.load('results_lindblad_312.npz', allow_pickle=True)#G=0,GH=0
m7,m8=MSD(data4['expect_values'],30,lent)
plt.plot(x,m7,linewidth=2.0,label='$\\uparrow$')
plt.plot(x,m8,':',linewidth=2.0,label='$\\downarrow$')
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(ncol=2,fontsize=20,prop=font,frameon=False)

plt.tight_layout()
plt.savefig('figsc1a.png',dpi=600,bbox_inches='tight')
plt.show()

data4 = np.load('results_lindblad_113.npz', allow_pickle=True)#G=0.3,GH=0
m7,m8=MSD(data4['expect_values'],30,lent)
plt.plot(x,m7,linewidth=2.0,label='$\\uparrow$')
plt.plot(x,m8,':',linewidth=2.0,label='$\\downarrow$')
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(ncol=2,fontsize=20,prop=font,frameon=False)

plt.tight_layout()
plt.savefig('figsc1c.png',dpi=600,bbox_inches='tight')
plt.show()

data4 = np.load('results_lindblad_114.npz', allow_pickle=True)#G=0.5,GH=0
m7,m8=MSD(data4['expect_values'],30,lent)
plt.plot(x,m7,linewidth=2.0,label='$\\uparrow$')
plt.plot(x,m8,':',linewidth=2.0,label='$\\downarrow$')
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(ncol=2,fontsize=20,prop=font,frameon=False)

plt.tight_layout()
plt.savefig('figsc1d.png',dpi=600,bbox_inches='tight')
plt.show()

data4 = np.load('results_lindblad_117.npz', allow_pickle=True)#G=1,GH=0
m7,m8=MSD(data4['expect_values'],30,lent)
plt.plot(x,m7,linewidth=2.0,label='$\\uparrow$')
plt.plot(x,m8,':',linewidth=2.0,label='$\\downarrow$')
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(ncol=2,fontsize=20,prop=font,frameon=False)

plt.tight_layout()
plt.savefig('figsc1e.png',dpi=600,bbox_inches='tight')
plt.show()

data4 = np.load('results_lindblad_123.npz', allow_pickle=True)#G=2,GH=0
m7,m8=MSD(data4['expect_values'],30,lent)
plt.plot(x,m7,linewidth=2.0,label='$\\uparrow$')
plt.plot(x,m8,':',linewidth=2.0,label='$\\downarrow$')
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(ncol=2,fontsize=20,prop=font,frameon=False)

plt.tight_layout()
plt.savefig('figsc1f.png',dpi=600,bbox_inches='tight')
plt.show()

data4 = np.load('results_lindblad_526.npz', allow_pickle=True)#G=0,GH=0.5
m7,m8=MSD(data4['expect_values'],30,lent)
plt.plot(x,m7,linewidth=2.0,label='$\\uparrow$')
plt.plot(x,m8,':',linewidth=2.0,label='$\\downarrow$')
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(ncol=2,fontsize=20,prop=font,frameon=False)

plt.tight_layout()
plt.savefig('figsc1g.png',dpi=600,bbox_inches='tight')
plt.show()

data4 = np.load('results_lindblad_537.npz', allow_pickle=True)#G=0,GH=3
m7,m8=MSD(data4['expect_values'],30,lent)
plt.plot(x,m7,linewidth=2.0,label='$\\uparrow$')
plt.plot(x,m8,':',linewidth=2.0,label='$\\downarrow$')
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(ncol=2,fontsize=20,prop=font,frameon=False)

plt.tight_layout()
plt.savefig('figsc1h.png',dpi=600,bbox_inches='tight')
plt.show()

data4 = np.load('results_lindblad_281.npz', allow_pickle=True)#G=0.3,GH=3
m7,m8=MSD(data4['expect_values'],30,lent)
plt.plot(x,m7,linewidth=2.0,label='$\\uparrow$')
plt.plot(x,m8,':',linewidth=2.0,label='$\\downarrow$')
plt.xlabel('time(fs)',font,fontsize=20)
plt.ylabel('MSD(t)',font,fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(ncol=2,fontsize=20,prop=font,frameon=False)

plt.tight_layout()
plt.savefig('figsc1i.png',dpi=600,bbox_inches='tight')
plt.show()
