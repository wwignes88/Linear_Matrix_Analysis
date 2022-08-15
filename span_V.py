# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:30:59 2022

@author: Donald
"""
import numpy as np
import Solve as S
def span_V(LIST) : #accepts list of vectors/ matrices [U0,U1,....]
    i = 1 ; V = LIST[0]
    while i < len(LIST): #Stack all matrices in list
        V = np.vstack([V,LIST[i]])
        i += 1
    
    VT  = V.transpose(); # vectors to be tested should be vertically orientated
    try:
        DIM = VT.shape ; L = DIM[0]; W = DIM[1] 
    except:
        if len(VT) != 1:
            return False, 1
        if len(VT) == 1:
            return True, 0       
    i   = 0
    #xxxprint('\n[span_v] W:  ',W)
    #xxxprint('[span_v] V^T: \n ',VT)
    while i < L: # L{VT} = W{V} 
        ei = np.zeros(L) ; ei[i] = 1 # basis vector
        Test = S.solve(VT,ei) # solves VT|ei
        
        if Test[0] == 'NA':
            #print(f'[span_v] system doesnt span e{i} ')
            return False,i
        i += 1
        
    if Test[0] == 'independent' or Test[0] == 'dependent':
        return True,i-1
    
    
        
        
    