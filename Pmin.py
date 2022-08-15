# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 08:27:26 2022

@author: Donald
"""
import numpy as np
import span_V as sp
import Solve as s

#------------------------------
def Poly_add(ak, Polyk):
    # ak= alpha_k is x vector of solution to Ux = 0
	# Polyk =  list of matrices: [I,(T**1)Pk, (T**2)Pk, ...] 
    P0 = Polyk[0]
    DIM = P0.shape ; L = DIM[0] ; W = DIM[1] 
    j = 0; Pk = 0*Polyk[0]
    #XXXprint(f'\nT^{j}*P:\n',Pk.shape)
    while j < len(Polyk):
        #XXXprint(f'T^{j}*P:\n',Polyk[j].shape)
        #XXXprint('ak: ',ak)
        Pk += ak[j]*Polyk[j]  # c.f. bottom of page 10 of reference
        j += 1
    return Pk # (matrix)


    
#-------------------------------


def P_min(T):
    DIM = T.shape ; L = DIM[0] ; W = DIM[1] #Note that W is the dimension of the space R{W}
    
    
    # see section 4.4 of paper
    Pk    = np.eye(L) ; Poly_k = [Pk]  # Start with P{k} = [I]
    zeros = np.zeros(W) # initiated for unit vectors
    
    k  = 0 ; K = -1
    ek = np.copy(zeros); ek[0]=1 ; PK = [] 
    Span = False
    while k < W:

        
        if k == 0:
            U = ek


        #--------Test if current system U spans R{W}:
        print(f'System: U{k-1}   :\n',U)  
        Span = sp.span_V([U])
        if Span[0] == True:
            print(f'\n[Pmin] [U0,U{k}] spans R{W}')
            return 


        
        #--------------
        
        Uk  = np.matmul(Pk,ek) #(T^0)*Pk*ek
        if k > 0:
            U = np.vstack([U,ek])
            print(f'System: U|e{k}   :\n',U)
            U = np.vstack([U,Uk]) # i= 0 term
            
            
            
        Ti  = np.eye(L);  # T^0 
        
        Poly_k = [Pk] ;   # [ (T**0)Pk ] - see pg. 10
        i = 1; Dep =  False
        while  Dep == False:  
            Ti   = np.matmul(Ti,T) 
            TiPk = np.matmul(Ti,Pk) 
            ui   = np.matmul(TiPk,ek) 
            Uk   = np.vstack([Uk,ui]) 
            U    = np.vstack([U,ui])
            Poly_k.append(TiPk)
            
            Test_Uk  = s.solve(Uk.transpose(),zeros)
            if Test_Uk[0] == 'dependent':
                pk  = Test_Uk[1]  ; 
                Uk  = np.delete(Uk,len(Uk)-1,0) ; print(f'U{k} independent:\n',Uk)
                U   = np.delete(U,len(U)-1,0)   ; #XXXprint('U :\n',U)
                globals()['U' + str(k)] = np.array(Uk)
                
                Test_U = s.solve(U.transpose(),zeros)[0]
                if Test_U == 'dependent':
                    print('U dependence detected...')
                    l = len(U);
                    while Test_U == 'dependent' :
                        l += -1
                        Test_U = s.solve(U[:l,:].transpose(),zeros)[0]    
                    U = U[:l,:]
                    print(f'U{l} independent:\n',U)
                    
                Dep = True # Will break the loop   
            i += 1




            
        #-------------------------------
        Span = sp.span_V([U])
        if Span[0] == True:
            print(f'\n[Pmin] [U0,U{k}] spans R{W}')
            return 
    
        #-------Create Polynomial Pk
        
        print(f'p{k}= ', pk)
        Pk  = Poly_add(pk, Poly_k)
        PK.append(Pk)
        globals()['P'+str(k)] = Pk
        
        #------- move to next unit vector that is not in span of system U
        k  = Span[1]
        print(f'[Pmin] system doesnt span e{k} ')
        ek = np.copy(zeros) ; ek[k]=1 
        print(f'\n\n***********k={k}')
        print(f'\n[Pmin] e{k}=',ek)             

A = np.matrix(' 0 1   0  0 -1 -1 ;\
               -3 8   5  5  2 -2 ;\
               1  0  -1  0 -1  0 ;\
               4 -10 -7 -6 -3  3 ;\
               -1 3   2  2  2 -1 ;\
               -2 6   4  4  2 -1')


P_min(A)







