import numbers
import sys
import os
os.system('cls')
import numpy  as np
import matplotlib.pyplot as plt
import math
from dominio_numerico import dominio_numerico
from dados_quadratura import dados_quadratura 
from tempo_mid_quadratico_biot_infinito import tempo_mid_quadratico_biot_infinito
from tempo_mis_quadratico_biot_infinito import tempo_mis_quadratico_biot_infinito
from tempo_mid_quadratico_biot_finito import tempo_mid_quadratico_biot_finito
from tempo_mis_quadratico_biot_finito import tempo_mis_quadratico_biot_finito 
from solucao_numerica_biot_finito import solucao_numerica_biot_finito
from  dados_numerico_tao_bio_infinito import dados_numerico_tao_bio_infinito
from dados_experimentais import dados_experimentais
from dominio_experimental import dominio_experimental
from gera_imagem_experiemetal import gera_imagem_experiemetal

from gera_imagem  import gera_imagem 

#Pontos de discrtização
N= 17
NP =10



espaco =np.zeros((N), dtype=np.longdouble)
raizes =np.zeros((NP), dtype=np.longdouble)
coeficinetes = np.zeros((NP), dtype=np.longdouble)
vetor_espaco_analitico =np.zeros((N), dtype=np.longdouble)


#Decaracao de variaveis
vetor_espaco_numerico = np.zeros((N), dtype=np.longdouble)



    
vetor_espaco_numerico = dominio_numerico()
vetor_espaco_analitico = vetor_espaco_numerico


print(vetor_espaco_numerico)
#Coecientes quadratura gaussiana 
raizes,coeficientes= dados_quadratura()
print(raizes)


#Ste numbers
vetor_ste = np.zeros((3), dtype=np.longdouble)
vetor_ste[0]=0.5
vetor_ste[1]=1.0
vetor_ste[2]=2.0
# Biot infinito.

legenda_biot_infinito =['Biot Infinito Ste =0.5.tiff ', 'Biot Infinito  Ste =1.0 .tiff', 'Biot Infinito Ste =2.0 .tiff'] 
legenda_biot_infinito_interna =['Biot = $\u221E$, Ste =0.5 ', 'Biot = $\u221E$,  Ste =1.0', 'Biot = $\u221E$, Ste =2.0 '] 


for i_ste in range(0,3):
       ste =vetor_ste[i_ste]
       legenda =legenda_biot_infinito[i_ste]
       legenda_interna =legenda_biot_infinito_interna[ i_ste]
       solucao_numerica_biot_infinito = dados_numerico_tao_bio_infinito(i_ste)
       vetor_tempo_mid_quadratico_biot_infinito = tempo_mid_quadratico_biot_infinito(vetor_espaco_numerico,raizes,coeficientes,ste,N,NP)
       vetor_tempo_mis_quadratico_biot_infinito = tempo_mis_quadratico_biot_infinito(vetor_espaco_numerico,raizes,coeficientes,ste,N,NP)
       gera_imagem(vetor_espaco_numerico, solucao_numerica_biot_infinito, vetor_tempo_mid_quadratico_biot_infinito,vetor_tempo_mis_quadratico_biot_infinito,legenda,legenda_interna)
       




#Biot finito
vetor_biot = np.zeros((2), dtype=np.longdouble)
vetor_biot[0] =2
vetor_biot[1] =10



# Lengendas
legenda =[ ['Biot =2 Ste =0.5 .tiff', 'Biot =2, Ste =1.0 .tiff', ' Biot =2, Ste =2.0 .tiff'], ['Biot =10, Ste =0.5 .tiff', 'Biot =10, Ste =1.0 .tiff' , 'Biot =10, Ste =2.0 .tiff'] ]
legenda_interna =[ ['Biot =2, Ste =0.5', 'Biot =2, Ste =1.0', ' Biot =2, Ste =2.0'], ['Biot =10, Ste =0.5', 'Biot =10, Ste =1.0' , 'Biot =10, Ste =2.0'] ]
for i_biot in range (0,2):
      biot = vetor_biot[i_biot]
      for j_ste  in range(0,3):
            ste = vetor_ste[j_ste]
            vetor_tempo_mid_quadratico_biot_finito = tempo_mid_quadratico_biot_finito(raizes, coeficientes,vetor_espaco_numerico,biot, ste,N,NP) 
                                                                                 
            vetor_tempo_mis_quadratico_biot_finito = tempo_mis_quadratico_biot_finito(raizes,coeficientes,biot,ste,vetor_espaco_numerico,N,NP)
            solucao_numerica =solucao_numerica_biot_finito(i_biot,j_ste)
            print(  solucao_numerica   )
            legenda_imagem =legenda[i_biot][j_ste]
            legenda_titulo= legenda_interna[i_biot][j_ste]
            #Gera imagens
            gera_imagem(vetor_espaco_numerico,solucao_numerica,vetor_tempo_mid_quadratico_biot_finito,vetor_tempo_mis_quadratico_biot_finito,legenda_imagem,legenda_titulo)
                   

# Lengendas
legenda_experimental =['Chumbo resfriado a ar - Bi=0.47  Ste=1.765 .tiff', 'Chumbo resfriado a água - Bi=4.2  Ste=1.765 .tiff', ' Estanho resfriado a água - Bi=2.8  Ste=0.910 .tiff', 'Estanho resfriado a ar - Bi=0.36  Ste=0.910 .tiff']
legenda_experimental_titulo =['Lead cooled by air, Bi=0.47 and  Ste=1.765', 'Lead cooled by water, Bi=4.2  and Ste=1.765', 'Tin cooled by water, Bi=2.8 and  Ste=0.910', 'Tin cooled by air,  Bi=0.36 and Ste=0.910' ]

espaco_experimental= dominio_experimental()
N= len(espaco_experimental)
biot_experimental=np.zeros(( 4), dtype=np.longdouble)
ste_experimental=np.zeros((4), dtype=np.longdouble)

biot_experimental[0]=0.47
biot_experimental[1]=4.2
biot_experimental[2]=2.8
biot_experimental[3]=0.36
ste_experimental[0]=1.765
ste_experimental[1]=1.765
ste_experimental[2]=0.910
ste_experimental[3]=0.910
for i in range(0,4):
      biot = biot_experimental[i]
      ste = ste_experimental[i]
      legenda =legenda_experimental[i]
      legenda_titulo = legenda_experimental_titulo[i]
      print(f'{legenda_titulo}')
      solucao_experimental =dados_experimentais(i)
      vetor_tempo_mid_quadratico_biot_finito = tempo_mid_quadratico_biot_finito(raizes, coeficientes,espaco_experimental,biot, ste,N,NP) 
      vetor_tempo_mis_quadratico_biot_finito = tempo_mis_quadratico_biot_finito(raizes,coeficientes,biot,ste,espaco_experimental,N,NP)
      gera_imagem_experiemetal(espaco_experimental,solucao_experimental, vetor_tempo_mid_quadratico_biot_finito,vetor_tempo_mis_quadratico_biot_finito,legenda,legenda_titulo)
            
     

