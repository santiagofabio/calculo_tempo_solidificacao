def dados_quadratura():
    import numpy as np


    raizes =np.zeros((10), dtype=np.longdouble)
    coeficinetes= np.zeros((10), dtype=np.longdouble)
  #raizes
    raizes[0] =0.973906528517172
    raizes[1]=0.865063366688985
    raizes[2] =0.679409568299024
    raizes[3] =0.433395394129247
    raizes[4] =0.148874338981631
    raizes[5] =-0.148874338981631 
    raizes[6] =-0.433395394129247
    raizes[7] =-0.679409568299024
    raizes[8] =-0.865063366688985
    raizes[9] =-0.973906528517172
  #Coeficientes

    coeficinetes[0]= 0.066671344308688
    coeficinetes[1]= 0.149451349150581
    coeficinetes[2]= 0.219086362550581
    coeficinetes[3]= 0.269266719309996
    coeficinetes[4]= 0.295524224714753
    coeficinetes[5]= 0.295524224714753
    coeficinetes[6]= 0.269266719309996
    coeficinetes[7]= 0.219086362515982
    coeficinetes[8]= 0.149451349150581
    coeficinetes[9]=0.066671344308688

    return(raizes,coeficinetes)    