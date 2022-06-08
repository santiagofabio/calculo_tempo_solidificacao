def tempo_mis_quadratico_biot_infinito(espaco,raizes,coeficientes,ste,N,NP):
    import math
    import numpy as np
    vetor_tempo_mis_quadratico = np.zeros((N), dtype=np.longdouble)


  
    for j in range (0,N):
        #Inicio da integração gaussiana MIS perfil quadrático
        a=0.0
        b=espaco[j]
        soma =0.0
        for d in range(0,NP):
              h1 =0.5*(b-a)
              h2 =0.5*(a+b)
              dx =0.5*(b-a)
              x =h1*raizes[d]+h2 # x faz o papel de epsilon aqui
              p=(((2.0*ste)/(1.0-x))+1.0)
              u = 1.0 - x
              termo1 =1.0/(-1-((2.0*u)/x)+((u/(ste*x))*((math.sqrt(p))-1.0)))
              termo2 = (((x*(x-2.0))/((12.0*u)*(math.sqrt(p))))+(x/6.0)-((u**2)/ste)-(1/3)+((1/(12*ste))*(-2.0 +(6.0*x)-(3.0*x*x))*((math.sqrt(p))-1.0))) 
              soma  = soma +   (termo1*termo2)*coeficientes[d]*dx
        vetor_tempo_mis_quadratico[j] = soma
     
    return( vetor_tempo_mis_quadratico)