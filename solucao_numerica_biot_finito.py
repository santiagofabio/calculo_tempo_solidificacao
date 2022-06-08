def solucao_numerica_biot_finito(i,j):
    import numpy as np
       

    matriz_numerica = np.zeros((2,3,17), dtype=np.longdouble)
    
    #Biot 2 Ste0.5
    matriz_numerica[0][0][0]=0.026
    matriz_numerica[0][0][1] =0.05246
    matriz_numerica[0][0][2]=0.1074
    matriz_numerica[0][0][3]=0.16378
    matriz_numerica[0][0][4] =0.22092
    matriz_numerica[0][0][5] = 0.27842
    matriz_numerica[0][0][6]= 0.33582 
    matriz_numerica[0][0][7]= 0.39284 
    matriz_numerica[0][0][8]= 0.44902
    matriz_numerica[0][0][9] =0.50404
    matriz_numerica[0][0][10]= 0.55754
    matriz_numerica[0][0][11]= 0.60918
    matriz_numerica[0][0][12]=0.65854
    matriz_numerica[0][0][13]= 0.70528
    matriz_numerica[0][0][14]=0.74896
    matriz_numerica[0][0][15]=0.78904
    matriz_numerica[0][0][16]= 0.82502

    #Biot 2 Ste 1.0
    matriz_numerica[0][1][0] = 0.01319
    matriz_numerica[0][1][1] =0.02655
    matriz_numerica[0][1][2]= 0.05543
    matriz_numerica[0][1][3]= 0.08576
    matriz_numerica[0][1][4] =0.1171
    matriz_numerica[0][1][5]= 0.1491
    matriz_numerica[0][1][6]= 0.18162
    matriz_numerica[0][1][7]=0.21418
    matriz_numerica[0][1][8]=0.24668
    matriz_numerica[0][1][9]=0.27894
    matriz_numerica[0][1][10]= 0.3108
    matriz_numerica[0][1][11]=0.34182
    matriz_numerica[0][1][12]=0.37185
    matriz_numerica[0][1][13]=0.40065
    matriz_numerica[0][1][14]=0.42789
    matriz_numerica[0][1][15]= 0.45327
    matriz_numerica[0][1][16]=0.47642

   

    #Biot 2 Ste 2.0
    matriz_numerica[0][2][0] =0.00681
    matriz_numerica[0][2][1]= 0.01361
    matriz_numerica[0][2][2]= 0.02931
    matriz_numerica[0][2][3] = 0.04632
    matriz_numerica[0][2][4] = 0.06432
    matriz_numerica[0][2][5] = 0.08317
    matriz_numerica[0][2][6]= 0.10253
    matriz_numerica[0][2][7] = 0.12241
    matriz_numerica[0][2][8]=0.14255
    matriz_numerica[0][2][9]=0.16257
    matriz_numerica[0][2][10]=0.18261
    matriz_numerica[0][2][11]=0.20254
    matriz_numerica[0][2][12]=0.22219
    matriz_numerica[0][2][13]=0.24123
    matriz_numerica[0][2][14]=0.25936
    matriz_numerica[0][2][15]=0.27654
    matriz_numerica[0][2][16]=0.29242
    
    #Biot 10 Ste  0.5
    matriz_numerica[1][0][0] =0.00666
    matriz_numerica[1][0][1] = 0.01386
    matriz_numerica[1][0][2]=0.03266
    matriz_numerica[1][0][3]= 0.05554
    matriz_numerica[1][0][4]=0.08188
    matriz_numerica[1][0][5]=0.11126
    matriz_numerica[1][0][6]=0.14312
    matriz_numerica[1][0][7] =0.17704
    matriz_numerica[1][0][8]=0.21246
    matriz_numerica[1][0][9]=0.2489
    matriz_numerica[1][0][10]=0.2859
    matriz_numerica[1][0][11]=0.32306
    matriz_numerica[1][0][12]=0.3598
    matriz_numerica[1][0][13]=0.39556
    matriz_numerica[1][0][14]=0.42982
    matriz_numerica[1][0][15] =0.46192
    matriz_numerica[1][0][16]=0.49126
    
    #Biot 10 Ste  1.0
    matriz_numerica[1][1][0] =0.00302
    matriz_numerica[1][1][1] =0.00691
    matriz_numerica[1][1][2] =0.0172
    matriz_numerica[1][1][3] =0.02989
    matriz_numerica[1][1][4] = 0.0447
    matriz_numerica[1][1][5] =0.06133
    matriz_numerica[1][1][6] =0.07957
    matriz_numerica[1][1][7] =0.09913
    matriz_numerica[1][1][8] =0.11974
    matriz_numerica[1][1][9] =0.14117
    matriz_numerica[1][1][10] =0.16306
    matriz_numerica[1][1][11] =0.18524
    matriz_numerica[1][1][12] =0.20743
    matriz_numerica[1][1][13] =0.22927
    matriz_numerica[1][1][14] =0.25032
    matriz_numerica[1][1][15] =0.27035
    matriz_numerica[1][1][16] =0.289

    matriz_numerica[1][2][0]=0.0016
    matriz_numerica[1][2][1]=0.0038
    matriz_numerica[1][2][2]=0.00972
    matriz_numerica[1][2][3]=0.01721
    matriz_numerica[1][2][4]=0.02601
    matriz_numerica[1][2][5]=0.03606
    matriz_numerica[1][2][6]=0.04717
    matriz_numerica[1][2][7]=0.05908
    matriz_numerica[1][2][8]=0.0718
    matriz_numerica[1][2][9]=0.08509
    matriz_numerica[1][2][10]=0.09887
    matriz_numerica[1][2][11]=0.11273
    matriz_numerica[1][2][12]=0.12666
    matriz_numerica[1][2][13]=0.14052
    matriz_numerica[1][2][14]=0.15416
    matriz_numerica[1][2][15]=0.16757
    matriz_numerica[1][2][16]=0.18024

    solucao_numerica =matriz_numerica[i][j][:]
    return(solucao_numerica)





