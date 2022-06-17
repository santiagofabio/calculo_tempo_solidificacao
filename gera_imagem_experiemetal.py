def gera_imagem_experiemetal(vetor_espaco_numerico,solucao_experimental,vetor_tempo_mid_quadratico,vetor_tempo_mis_quadratico,legenda_imagem,legenda_titulo):
     import matplotlib.pyplot as plt
     import matplotlib.ticker as ticker
     import numpy as np
     fig = plt.figure(figsize=(10, 6))
     ax1 = fig.tight_layout()
     ax1 = fig.add_axes([0.1, 0.1, 0.85, 0.85]) # axes principal
     #ax2 = fig.add_axes([0.55, 0.2, 0.35, 0.25]) # axes interno
     
     # figura principal
     ax1.margins(0.0,0.0)
     n =len(solucao_experimental)-1
     inicio_y = solucao_experimental[0]
     fim_y = solucao_experimental[n]
     passo_y = (solucao_experimental[n]-solucao_experimental[0])/n
     #plt.yticks(np.arange(inicio,fim ))
     ax1.yaxis.set_ticks(np.arange( inicio_y,fim_y +1,passo_y))
     
     inicio_x = vetor_espaco_numerico[0]
     fim_x = vetor_espaco_numerico[n]
     passo_x = vetor_espaco_numerico[1]-vetor_espaco_numerico[0]
     ax1.xaxis.set_ticks(np.arange( inicio_x,fim_x +1,passo_x))


    # plt.yticks(np.arange(min(vetor_espaco_numerico)), max(vetor_espaco_numerico)+1)
     ax1.plot(vetor_espaco_numerico,solucao_experimental,'o', lw=1, label='Experimental solution  (Milanez & Ismael (1984))' ) 
     ax1.plot(vetor_espaco_numerico,vetor_tempo_mis_quadratico,'b',lw=1,label='SIM - quadratic profile (Milanez & Ismael (1984))')
     ax1.plot(vetor_espaco_numerico,vetor_tempo_mid_quadratico, 'm', lw=1, label='DIM - quadratic profile (present work)')


     ax1.set_xlabel('thermal penetration depth $(\epsilon)$')
     ax1.set_ylabel('dimensionless time $(\u03C4)$ ')
     ax1.set_title(legenda_titulo)
     legend = ax1.legend(loc= 'upper left')
     
     
     print(f'{legenda_titulo}')

    
     """
     vetor_espaco_interno =vetor_espaco_numerico[7:11]
     vetor_tempo_mis_quadratico_interno =vetor_tempo_mis_quadratico[7:11]
     vetor_tempo_mid_quadratico_interno =vetor_tempo_mid_quadratico[7:11]
     solucao_experimental_interno =  solucao_experimental[7:11]

     ax2.plot(vetor_espaco_interno, vetor_tempo_mis_quadratico_interno,'b',lw=1 )
     ax2.plot(vetor_espaco_interno,vetor_tempo_mid_quadratico_interno,'m',lw=1 )
     ax2.plot(vetor_espaco_interno, solucao_experimental_interno,'o', lw=1)"""

     plt.savefig(legenda_imagem, dpi =300, format='tiff')
     plt.show()
     plt.close()

     return(0)