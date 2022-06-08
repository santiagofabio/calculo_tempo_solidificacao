def  dados_experimentais(indice):
   import numpy as np

   matriz_experimental = np.zeros((4,12), dtype=np.longdouble)
   """
   
    1 - Chumbo resfriado a ar - Bi=0.47  Ste=1.765'
    2 - CHUMBO RESFRIADO A ÁGUA - Bi=4.2  Ste=1.765'
    3 - Estanho resfriado a água - Bi=2.8  Ste=0.910'
    4 - Estanho resfriado a ar - Bi=0.36  Ste=0.910'
   
   """



   #Chumbo ar 
   matriz_experimental[0][0] =0.0446
   matriz_experimental [0][1]= 0.105
   matriz_experimental [0][2]= 0.1627
   matriz_experimental [0][3]= 0.2199
   matriz_experimental [0][4]= 0.2772
   matriz_experimental [0][5]= 0.3218
   matriz_experimental [0][6]= 0.3772
   matriz_experimental [0][7]= 0.4219
   matriz_experimental [0][8]= 0.4646
   matriz_experimental [0][9]= 0.5183
   matriz_experimental [0][10]= 0.5575
   matriz_experimental [0][11]= 0.6057

   # Chumborefrigerado agua
   constante =(1.905*10**(-5))/(0.1*0.1)
   matriz_experimental [1][0]= 4.4*constante
   matriz_experimental [1][1]= 8.2*constante
   matriz_experimental [1][2]= 12.5*constante
   matriz_experimental [1][3]= 18.6*constante
   matriz_experimental [1][4]= 26.1*constante
   matriz_experimental [1][5]= 34.8*constante
   matriz_experimental [1][6]= 44.4*constante
   matriz_experimental [1][7]= 54.4*constante
   matriz_experimental [1][8]= 65.1*constante
   matriz_experimental [1][9]= 76.0*constante
   matriz_experimental [1][10]= 87.4*constante
   matriz_experimental [1][11]= 98.7*constante



   # Agua e estanho 
   matriz_experimental[2][0]= 0.0214
   matriz_experimental[2][1]= 0.0404
   matriz_experimental[2][2]= 0.0631
   matriz_experimental[2][3]= 0.0893
   matriz_experimental[2][4]= 0.1155
   matriz_experimental[2][5]= 0.1466
   matriz_experimental[2][6]= 0.1812
   matriz_experimental[2][7]= 0.2086
   matriz_experimental[2][8]= 0.2432
   matriz_experimental[2][9]= 0.2767
   matriz_experimental[2][10]= 0.3065
   matriz_experimental[2][11]= 0.3363

   #Estanho ar 
   matriz_experimental[3][0]= 0.1280
   matriz_experimental[3][1]= 0.2668
   matriz_experimental[3][2]= 0.4019
   matriz_experimental[3][3]= 0.5192
   matriz_experimental[3][4]= 0.6363
   matriz_experimental[3][5]= 0.7357
   matriz_experimental[3][6]= 0.8421
   matriz_experimental[3][7]= 0.9378
   matriz_experimental[3][8]= 1.0299
   matriz_experimental[3][9]= 1.1184
   matriz_experimental[3][10]= 1.2033
   matriz_experimental[3][11]= 1.2775

   solucao =matriz_experimental[indice][:]
   return(solucao)

