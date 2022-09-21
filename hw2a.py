#HW2a:將u、v分量轉為風向、風速
# 
#weshengjie   111/09/20


import math as m


#列出Ｕ、V各四個數值
U=[1.112,1.050,1.998,-1.489]
V=[2.164,1.483,0.377,-0.289]

#建立兩個空陣列WS和WD
WS=[]
WD=[]


for i in range(4):
    #將U、V轉為浮點數,並賦值給變數u、v
    u=float(U[i])
    v=float(V[i])

    #將u和v轉換成風速，並存入WS陣列裡
    WS.append(round((u**2+v**2)**(1/2),3))

    #將u和v轉換成風向
    THETA=m.degrees(m.atan(v/u))
    if u<0:
        PHI=90-THETA
    elif u>0:
        PHI=270-THETA
    elif u==0 & v>0:
        PHI=180
    elif u==0 & v<0:
        PHI=0
    elif u==0 & v==0:
        print("No wind")

    #將得到的PHI值存入WD陣列裡
    WD.append(round(PHI,1))

#輸出WS和WD
print(WS)
print(WD)
