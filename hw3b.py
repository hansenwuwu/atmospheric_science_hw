'''hw3b
solve a differential equation by Euler method and plot a figure

wushengjie 111/09/27
'''

import numpy as np
import matplotlib.pyplot as plt

#setting up time array, S array, I array, and R array
t=np.linspace(0,5,501)
S=np.zeros(501)
I=np.zeros(501)
R=np.zeros(501)

#setting up initial values
S[0]=10000.
I[0]=10.
R[0]=0.

#setting up constants
ß=0.0005
r=0.5
dt=0.01

#iterate for the sequence
for i in range(500):
    #calculate S array, I array, R array
    S[i+1]=S[i]-ß*I[i]*S[i]*dt
    I[i+1]=I[i]+(ß*I[i]*S[i]-I[i]*r)*dt
    R[i+1]=R[i]+r*I[i]*dt

#plotting solutions
plt.plot(t,S,color='orange',marker='')
plt.plot(t,I,'g-',t,R,'b-')
plt.title(r'$S_{0}$=10000, $I_{0}$=10, $\beta$=0.0005, $\gamma$=0.5',fontsize=15)
plt.xlabel('Month',fontsize=15)
plt.ylabel('Population',fontsize=15)
plt.xticks(np.linspace(0,5,6))
plt.xlim([0,5])
plt.yticks(np.linspace(0,12000,7))
plt.ylim([0,12000])
plt.legend(['S','I','R'],loc='upper right')

#save the figure into hw3b.png
plt.savefig('hw3b.png')
#display the current figure
plt.show()