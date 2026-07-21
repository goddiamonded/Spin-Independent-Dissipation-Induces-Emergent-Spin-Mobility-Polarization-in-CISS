# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:20:10 2026

@author: 83837
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def MSD(pop,nM,lent):
  m7=[]
  m8=[]
  for i in range(lent):
    a=0
    b=0
    for j in range(nM*4+4):
        if j%4==2:
            a+=((j+2)/4)**2*(pop[j][i]) 
            b+=((j+2)/4)**2*(pop[j+1][i])
        elif j%4==0:
            a+=(j/4)**2*(pop[j][i])
            b+=(j/4)**2*(pop[j+1][i])         
    m7.append(a/nM) 
    m8.append(b/nM)
  return m7,m8

def lr(m1,m2,t1,t2,t3,t4,lent,flag=False):
    model = LinearRegression()  # LinearRegression
    x=[]
    for i in range(t1,t2,1):
       x.append(i*27.211*2.419/100/0.12*0.5)  #unit conversion，1/(0.12)*0.5*27.211au time
    x=np.array(x)
    y=np.array(m1[t1:t2])
    model.fit(x.reshape(-1,1), y.reshape(-1,))
    a=model.coef_[0]
    b=model.intercept_

    x1=[]
    for i in range(t3,t4,1):
       x1.append(i*27.211*2.419/100/0.12*0.5)
    x1=np.array(x1)   
    y1=np.array(m2[t3:t4])
    model.fit(x1.reshape(-1,1), y1.reshape(-1,))
    a1=model.coef_[0]
    b1=model.intercept_
    
    yfit=a*x+b
    mean_y = np.mean(y)
    total_sum_of_squares = np.sum((y - mean_y) ** 2)
    residual_sum_of_squares = np.sum((y - yfit) ** 2)
    r_squared = 1 - (residual_sum_of_squares / total_sum_of_squares)
    #print(r_squared)
    
    yfit1=a1*x1+b1
    mean_y1 = np.mean(y1)
    total_sum_of_squares = np.sum((y1 - mean_y1) ** 2)
    residual_sum_of_squares = np.sum((y1 - yfit1) ** 2)
    r_squared1 = 1 - (residual_sum_of_squares / total_sum_of_squares)
    #print(r_squared1)
    #print("D:", a+a1)
    
    #print('Ps:', (a-a1)/(a+a1)) 
    
    x=[]
    for m in range(lent):
        x.append(m*27.211*2.419/100/0.12*0.5)
    x=np.array(x)    
    
    yfit=a*x+b
    
#plt.plot(x,m1d[:i],'-.',linewidth=2.0,label='$\\downarrow$')
    yfit1=a1*x+b1
     
    if  flag==False:
        return r_squared,r_squared1,a,a1
    else:
        plt.plot(x,m1[:],linestyle='--',label='$\\uparrow$')
        plt.plot(x[t1:t2],yfit[t1:t2],linewidth=2.0,label='$\\uparrow$,linear fit')
        plt.plot(x[t3:t4],yfit1[t3:t4],linewidth=2.0,label='$\\downarrow$,linear fit')
#plt.plot(x,m3u[:i],'--',linewidth=2.0,label='$\\uparrow$,purely ele')
        plt.plot(x,m2[:],':',linewidth=2.0,label='$\\downarrow$,purely electronic')
        print(r_squared,r_squared1)
        print("D:", a+a1)
        return a,a1