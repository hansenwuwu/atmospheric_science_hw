'''hw3a
plot four graphs relatively for wind speed-time graph, wind direction-time graph, u-component-time graph, v-component-time graph 

wushengjie 111/09/27
'''

import readline
import numpy as np
import matplotlib.pyplot as plt


#read from hw3_data.txt
date,time,WS,WD=np.loadtxt('hw3_data.txt',skiprows=1,unpack='True',dtype='U5,U5,f8,f8')

#transfer WS into u and v
u=WS*np.cos(np.radians(270-WD))
v=WS*np.sin(np.radians(270-WD))

#split window
f, ax=plt.subplots(2,2,sharex='all',sharey='none',figsize=(10,6))

#upper left
ax[0,0].plot(time[0:24],WS[0:24],'r--',time[24:48],WS[24:48],'g--',time[48:72],WS[48:72],'b--')
ax[0,0].set_title(r'Wind speed',fontsize=15)
ax[0,0].set_xlim([0,24])
ax[0,0].set_ylim([0,8])
ax[0,0].set_xticks(np.linspace(0,24,7),['0','4','8','12','16','20','24'])
ax[0,0].set_yticks(np.linspace(0,8,5))
ax[0,0].set_ylabel('(m/s)',fontsize=15)
ax[0,0].legend(['20171127','20171128','20171129'],loc='upper right')

#upper right
ax[0,1].plot(time[0:24],WD[0:24],'r--',time[24:48],WD[24:48],'g--',time[48:72],WD[48:72],'b--')
ax[0,1].set_title(r'Wind direction',fontsize=15)
ax[0,1].set_ylabel('(degree)',fontsize=15)
ax[0,1].set_ylim([0,360])
ax[0,1].set_yticks(np.linspace(0,360,9))

#lower left
ax[1,0].plot(time[0:24],u[0:24],'r--',time[24:48],u[24:48],'g--',time[48:72],u[48:72],'b--')
ax[1,0].set_title(r'U-component wind',fontsize=15)
ax[1,0].set_xlabel('Time(hour)',fontsize=15)
ax[1,0].set_ylabel('(m/s)',fontsize=15)
ax[1,0].set_ylim([-8,8])
ax[1,0].set_yticks(np.linspace(-8,8,9))

#lower right
ax[1,1].plot(time[0:24],v[0:24],'r--',time[24:48],v[24:48],'g--',time[48:72],v[48:72],'b--')
ax[1,1].set_title(r'V-component wind',fontsize=15)
ax[1,1].set_xlabel('Time(hour)',fontsize=15)
ax[1,1].set_ylabel('(m/s)',fontsize=15)
ax[1,1].set_ylim([-8,8])
ax[1,1].set_yticks(np.linspace(-8,8,9))

plt.savefig('hw3a.png')
plt.show()

#combine 
data=np.array(list(zip(date,time,u,v,WS,WD)),dtype=[('date','U5'),('time','U5'),('u','f8'),('v','f8'),('WS','f8'),('WD','f8')])

#output to hw3a.txt
np.savetxt('hw3a.txt',data,comments='',fmt='%-6s%-7s%-+7.2f%-+7.2f%-8.3f%-5.1f',header='Date  Time   u[m/s] v[m/s] WS[m/s] WD[deg]')
