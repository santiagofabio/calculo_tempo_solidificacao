def tempo_mid_quadratico_biot_infinito(espaco,raizes,coeficientes,ste,N,NP):
                                         
    import numpy as np
    import math
    vetor_tempo_mid_quadratico = np.zeros((N), dtype=np.longdouble)
    
    for j in range (1,N):
         a=0.0
         b=espaco[j]
       
         #Integraçao gaussiana MID perfil quadrático
         soma1 =0.0  
         for f in range(0,NP):    
              h12 =0.5*(b-a)
              h22 =0.5*(a+b)
              dx =0.5*(b-a)
              x =h12*raizes[f]+h22; # x faz o papel de epsilon aqui
              u=1-x
              B=(-1+((u/(ste*x))*((math.sqrt((2*ste/u)+1))-1)))
              C=((B*x-u)/(x*x))
              termo12 =(1/((u*x)+(B*(x-x*x))+(C*((2*x*x*x/3)-x*x))))
              r=(1.0/ste)*(((-1.0/(x*x))*((math.sqrt(((2.0*ste)/(1.0-x))+1.0))-1.0))+((ste*(1-x))/(x*((1-x)**(3/2))*(math.sqrt(-x+2.0*ste+1.0)))))
              s=(1.0/ste)*(((-(2.0-x)/(x*x*x))*((math.sqrt(((2.0*ste)/(1.0 -x))+1.0))-1.0))+((ste*(1.0-x))/(x*x*((1.0-x)**(3/2))*(math.sqrt(-x+2*ste+1.0)))))
              termo22 = ((((x**3)/3)-((x**4)/4))*r +(-((x**4)/4)+((x**5)/5))*s +(x/6)-(x*x/10)+((u**2)*x/ste))
              soma1  = soma1 +   (termo12*termo22)*coeficientes[f]*dx

         
         vetor_tempo_mid_quadratico[j]= soma1
    return(vetor_tempo_mid_quadratico)


