def tempo_mid_quadratico_biot_finito(raizes, coeficientes, espaco,biot, ste,N,NP):
    import math
    import numpy as np 
    vetor_tempo_mid_biot_finito =np.zeros((N), dtype=np.longdouble)
    for j in range (0,N):
            a=0.0
            b = espaco[j]
         
            soma1 =0.0
            #Integraçao gaussiana MID perfil quadrático
            for z in range (0,NP):
                   h12 =0.5*(b-a)
                   h22 =0.5*(a+b)
                   dx  = 0.5*(b-a)
                   x =h12*raizes[z]+h22 # x faz o papel de epsilon aqui
                   u= 1-x
                   v= (biot-1)
                   a1  =(2.0*ste*biot*(x*x*v +2.0*x))
                   b1= (u*((x*v+1)**2))
                   p=((a1/b1) +1)
                   B = -1 + (((u)/(ste))*((x*v+1)/(x*x*v+2*x)))*((math.sqrt(p)) - 1)
                   db=((biot/(math.sqrt(p)))*((2/(x*x*v+2*x))-(2*v/((x*v+1)**2))+(1/(u*(x*v+1)))))-((1/ste)*((math.sqrt(p))-1)*((v/(x*x*v+2*x))+((x*x*v+2)/((x*x*v+2*x)**2))))
                   C=(((B*(1+x*v))-(u*v))/(x*x*v+2*x))
                   termo12 =(1/((u*x)+(B*(x-x*x))+(C*((2*x*x*x/3)-x*x))))
                   d=((((x*x*v+2*x)*(((1+x*v)*db)+(B*v)))-(B*(1+x*v)*(2*x*v+2)))/((x*x*v+2*x)**2))
                   e=((((x*x*v+2*x)*(((x+x*x*v)*db)+(B*(1+2*x*v))))-(B*(x+x*x*v)*(2*x*v+2)))/((x*x*v+2*x)**2))
                   f=((((x*x*v+2*x)*(((x*x+x*x*x*v)*db)+(B*(2*x+3*x*x*v))))-(B*(x*x+x*x*x*v)*(2*x*v+2)))/((x*x*v+2*x)**2))
                   g=(-v/((x*x*v+2*x)**2))*((-(x**4)/2)+(11*(x**5)/10)-(41*(x**6)/60)+(2*(x**7)/15)+(biot*((-(x**5)/6)+(7*(x**6)/20)-(2*(x**7)/15))))
                   termo22 = ((((x**2)/2)-((x**3)/3))+(((-(x**3)/3)+((x**4)/4))*db)+((((x**2)/2)-((x**3)/3))*(x*db+B))+(((-(x**4)/4)+((x**5)/5))*d)+((((2*x*x*x)/3)-((x**4)/2))*e)+(((-(x**2)/2)+((x**3)/3))*f)+(g)+((u**2)*x/ste))
                   soma1  = soma1 +   (termo12*termo22)*coeficientes[z]*dx
            vetor_tempo_mid_biot_finito[j]= soma1
    return(vetor_tempo_mid_biot_finito)
             

