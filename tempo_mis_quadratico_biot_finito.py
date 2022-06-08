def tempo_mis_quadratico_biot_finito(raizes,coeficientes,biot,ste,espaco,N,NP):
                                     
    import math
    import numpy as np
    vetor_tempo_mis_quadratico_biot_finito =np.zeros((N), dtype=np.longdouble)
    
    for j in range (0,N):
         a=0.0
         b=espaco[j]
         x=espaco[j]
         soma =0.0
         for d in range(0,NP):
             h1 =0.5*(b-a)
             h2 =0.5*(a+b)
             dx =0.5*(b-a)
             x =h1*raizes[d]+h2 # x faz o papel de epsilon aqui
             u=1-x
             v= biot-1.0
             p=(((2*ste*biot*(x*x*v+2*x))/(u*((x*v+1)**2)))+1)
             B=-1+(((u)/(ste))*((x*v+1)/(x*x*v+2*x)))*((math.sqrt(p))-1)
             db=((biot/(math.sqrt(p)))*((2/(x*x*v+2*x))-(2*v/((x*v+1)**2))+(1/(u*(x*v+1)))))-((1/ste)*((math.sqrt(p))-1)*((v/(x*x*v+2*x))+((x*x*v+2)/((x*x*v+2*x)**2))))
             t1=(-biot*(2*u-x*B)/(x*v+2))**(-1)
             t2=(-((u**2)/ste)+(1/(x*v+2))*(((v)*((4*x/3)-(13*x*x/4)+(5*x*x*x/3)))+(2-6*x+3*x*x)+(((((x**4)/12)-((x**3)/6))*v+(((x**3)/4)-(2*x*x/3)))*db)+ B*(((x*x*x/3)-(x*x/2))*v+((2*x*x/4)-(4*x/3))))-((v/((x*v+2)**2))*(v*((2*x*x/3)-(13*x*x*x/12)+(5*x*x*x*x/12))+(2*x-3*x*x+x*x*x)+B*(((x*x*x*x/12)-(x*x*x/6))*v+((x*x*x/4)-(2*x*x/3)))))-(u**2))
             soma  = soma +   (t1*t2)*coeficientes[d]*dx
         vetor_tempo_mis_quadratico_biot_finito[j]= soma
    return(vetor_tempo_mis_quadratico_biot_finito)
