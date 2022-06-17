def gera_imagem(vetor_espaco_numerico, solucao_numerico,vetor_tempo_mid_quadratico,vetor_tempo_mis_quadratico,legenda_imagem,legenda_titulo):
     import matplotlib.pyplot as plt
     import numpy as np
     fig = plt.figure(figsize=(10, 6))
     
     
    
     ax1 = fig.tight_layout()
     ax1 = fig.add_axes([0.1, 0.1, 0.85, 0.85]) # axes principal
     # figura principal
     ax1.margins(0.0,0.0)

     n =len(solucao_numerico)-1
     inicio_y = solucao_numerico[0]
     fim_y = solucao_numerico[n]
     passo_y = (solucao_numerico[n]-solucao_numerico[0])/n
     
     print(f'{inicio_y}')
     print(f'{fim_y}')
     print(f'{passo_y}')
     
     
     
     ax1.yaxis.set_ticks(np.arange( inicio_y,fim_y+1, passo_y))

     
     inicio_x = vetor_espaco_numerico[0]
     fim_x = vetor_espaco_numerico[n]
     passo_x = (vetor_espaco_numerico[n]-vetor_espaco_numerico[0])/n
     ax1.xaxis.set_ticks(np.arange( inicio_x,fim_x+1 ,passo_x))




     ax1.plot(vetor_espaco_numerico,solucao_numerico,'k--', lw=1, label='Tao numerical solution' ) 
     ax1.plot(vetor_espaco_numerico,vetor_tempo_mis_quadratico,'b',lw=1,label='SIM - quadratic profile (Milanez & Ismael (1984))')
     ax1.plot(vetor_espaco_numerico,vetor_tempo_mid_quadratico, 'm', lw=1, label='DIM - quadratic profile (present work)')
     n =len(vetor_espaco_numerico)
     
   
     
     ax1.set_xlabel('thermal penetration depth $(\epsilon)$' )
     #ax1.yaxis.set_ticks(np.arange(min(eixo_y), max(eixo_y),0.1))
     ax1.set_ylabel('dimensionless time $(\u03C4)$ ')
     ax1.set_title(legenda_titulo)
     legend = ax1.legend(loc= 'upper left')
     print(f'{legenda_imagem}')

     plt.savefig(legenda_imagem, dpi =300, format='tiff') 
     plt.show()
     plt.close()

     return(0)