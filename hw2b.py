#使用open、write 讀寫檔案
#
#wushengjie 111/09/20

import math as m


#開啟hw_data.txt
f1=open('hw2_data.txt','r')

#開啟新檔hw2b.txt
f2=open('hw2b.txt','w+')
#輸出檔頭
f2.write('Time[hh:mm] u[m/s] v[m/s] WS[m/S] WD[deg]\n')

#讀掉檔案中的第一行
a=f1.readline()

#讀入時間、風速、風向
for i in range(24):
    b=f1.readline()
    data=b.split(' ')
    WS=float(data[7])
    WD=float(data[-1])

    #將風向角度轉為弧度
    THETA=m.radians(270-WD)

    #計算u分量並賦值
    u=round(WS*m.cos(THETA),1)
    #計算v分量並賦值
    v=round(WS*m.sin(THETA),1)
    
    #將時間、計算出的u、v分量、WD、WS讀入
    if u<0:
        f2.write(str(data[0])+'      '+str(u)+'    '+str(v)+'    '+str(round(WS,1))+'     '+str(round(WD,1))+'\n')
    elif v<0:
        f2.write(str(data[0])+'       '+str(u)+'   '+str(v)+'    '+str(round(WS,1))+'     '+str(round(WD,1))+'\n')
    else:
        f2.write(str(data[0])+'       '+str(u)+'    '+str(v)+'    '+str(round(WS,1))+'     '+str(round(WD,1))+'\n')
    
#關閉hw2_data.txt和hw2b.txt
f1.close()
f2.close()
