# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:28:13 2021

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:25:46 2021

@author: user
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

def graph(X=[], savefolder ='./runs/', typeof='accuracy', Xlab='epoches'):
    plt.figure()
    
    plt.title('graph')
    
    coloring = 'purple'
  
    ax = plt.gca()
   
    
    #ax.axes.yaxis.set_visible(False)
    #plt.yticks(np.arange(0, 1))
    
    plt.xlabel(Xlab, labelpad=int(1))
    plt.ylabel(typeof)
  
    
    plt.plot(X, label=typeof, color='blue', marker='D', 
             markersize =2, markerfacecolor='blue')
 
    plt.savefig(savefolder+typeof+'.jpg')
   
    

   
    plt.legend()
    plt.close()


acc1 = []


with open("./runs/joint_accuracy.txt","r") as f:
   
    for i in f.readlines():
       acc1.append((float)(i.split(" ")[2]))



print(max(acc1))
graph(acc1) 