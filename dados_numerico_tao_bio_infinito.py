def dados_numerico_tao_bio_infinito(indice):
    import numpy as np
    dominio_tao  =np.zeros((17), dtype=np.longdouble)
    matriz_numerica =np.zeros((3,17), dtype=np.longdouble)
   
  
   
   
    
    #Biot infinito Ste =0.1
    """matriz_numerica[0][0]=0.0032
    matriz_numerica[0][1]=0.0154
    matriz_numerica[0][2]=0.057
    matriz_numerica[0][3]= 0.1194
    matriz_numerica[0][4]=0.2001
    matriz_numerica[0][5]=0.2967
    matriz_numerica[0][6]=0.4066
    matriz_numerica[0][7]=0.5273
    matriz_numerica[0][8]=0.6563
    matriz_numerica[0][9]=0.7912
    matriz_numerica[0][10]=0.9293
    matriz_numerica[0][11]=1.0682
    matriz_numerica[0][12]=1.2054
    matriz_numerica[0][13]=1.3383  
    matriz_numerica[0][14]=1.4644
    matriz_numerica[0][14]=1.581
    matriz_numerica[0][16]=1.6857"""

    #Biot infinito Ste =0.5
    matriz_numerica[0][0]=0.00072 
    matriz_numerica[0][1]=0.00316
    matriz_numerica[0][2]=0.01196
    matriz_numerica[0][3]=0.02558
    matriz_numerica[0][4]=0.0435
    matriz_numerica[0][5]=0.06518
    matriz_numerica[0][6]=0.09006
    matriz_numerica[0][7]=0.11776
    matriz_numerica[0][8]=0.14766
    matriz_numerica[0][9]=0.17926
    matriz_numerica[0][10]=0.21198
    matriz_numerica[0][11]=0.24532
    matriz_numerica[0][12]=0.27882
    matriz_numerica[0][13]=0.31186
    matriz_numerica[0][14]=0.34378
    matriz_numerica[0][15]=0.374
    matriz_numerica[0][16]=0.40198

    #Biot infinito Ste =1.0
    matriz_numerica[1][0]=0.0004
    matriz_numerica[1][1]= 0.00162
    matriz_numerica[1][2]=0.00631
    matriz_numerica[1][3]=0.01376
    matriz_numerica[1][4]=0.02371
    matriz_numerica[1][5]=0.03587
    matriz_numerica[1][6]=0.04994
    matriz_numerica[1][7]=0.06575
    matriz_numerica[1][8]=0.08301
    matriz_numerica[1][9]=0.10125
    matriz_numerica[1][10]=0.12038
    matriz_numerica[1][11]=0.14007
    matriz_numerica[1][12]=0.1601
    matriz_numerica[1][13]=0.17995
    matriz_numerica[1][14]= 0.19949
    matriz_numerica[1][15]=0.21819
    matriz_numerica[1][16]=0.23571
    

    matriz_numerica[2][0]=0.00024
    matriz_numerica[2][1]=0.00085
    matriz_numerica[2][2]=0.00346
    matriz_numerica[2][3]=0.00769
    matriz_numerica[2][4]=0.01354
    matriz_numerica[2][5]=0.0209
    matriz_numerica[2][6]=0.02936
    matriz_numerica[2][7]=0.03883
    matriz_numerica[2][8]=0.04939
    matriz_numerica[2][9]=0.06082
    matriz_numerica[2][10]=0.07285
    matriz_numerica[2][11]=0.08545
    matriz_numerica[2][12]=0.09813
    matriz_numerica[2][13]=0.11076
    matriz_numerica[2][14]=0.12331
    matriz_numerica[2][15]=0.13556
    matriz_numerica[2][16]=0.14737





    solucao =matriz_numerica[indice][:]
    return(solucao )















