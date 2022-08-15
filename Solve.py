import numpy as np
import sympy as sy
from scipy import linalg


def Gauss(M,v=None):
    M = np.array(M)
    A = np.copy(M)
    try:
        #xxxprint('...[Gauss]: Augmenting...')
        AT = A.transpose()
        Mv = np.vstack([AT,v]).transpose() # Augmented matrix M|v
        Reduced_Matrix  = sy.Matrix(Mv).rref()[0]  # convert to scypy matrix, gaussian eliminate
        
        # convert to numpy matrix:
        np_matrix       = np.array(Reduced_Matrix).astype(np.float64) 
        DIM = np_matrix.shape ; 
        L = DIM[0] ; W = DIM[1]
        
        MATRIX = np_matrix[:,:W-1]
        VECTOR = np_matrix[:, W-1]
        return (MATRIX,VECTOR)
    
    except:
        #xxxprint('...[Gauss]: excepted (error occurred)...')
        Reduced_Matrix  = sy.Matrix(A).rref()[0]
        # convert to numpy matrix:
        np_matrix       = np.array(Reduced_Matrix).astype(np.float64)
        return (np_matrix)

def solve(M,v):
    Print = True
    if print == True:
        print('\n\n##################\
              SOLVE\n\n###################')
    try:
        DIM = M.shape ; L = DIM[0] ; W = DIM[1] ; 
    except:
        W = 1; L = len(M)
        
        
    #xxxprint(f'\n[solve]: M: \n',M)
    #GAUSSIAN REDUCE:
    GAUSS = Gauss(M,v)
    M = GAUSS[0]; v = GAUSS[1]
    print(f'\n[solve]: M_reduced: \n',M)
    #xxxprint(f'[solve]: v_reduced: ',v)
    
    # Create NXN matrix
    if L > W:
        #Check if solution exists:
        i = W # check bottom zero rows to see if v[j] != 0
        while i < L:
            if v[i] != 0 and (M[i,:] == 0).all():
                if Print == True:
                    print(f'{i}....system not solvable...')
                return ('NA',np.nan*np.zeros(L))
            i += 1
                    
    
        # Delete rows for j>W
        row_delete = np.arange(W,L,1)
        #xxxprint('\nW,L:',W,L)
        #xxxprint(f'[solve]: row_delete: ',v)
        M = np.delete(M,row_delete,0)
        #xxxprint(f'[solve]: M after deleted: \n',M)

    if W > L: 
        # append additional rows of zeros for al L<j<W
        M = np.vstack([M,np.zeros([W-L,W])]) 
        v = np.append(v,np.zeros(W-L))
    
    # reset dimensions (should be NXN matrix now)
    N = len(M)
    N=W # W is number of variables to be solved for
    #xxxprint(f'\n[solve]: M_nxn: \n',M)

    
    # Count Dependent variables with Mii = 0;
    i = 0
    DEP = np.array([])
    while i < W:
        if M[i,i] == 0:
            DEP = np.append(DEP,i)
        i += 1  
    n_DEP = len(DEP)



    
    
    # ---------------  Independence:  
    if n_DEP == 0:
        if Print == True:
            print('...independence determined...')
    
        N
        # solve for x varibles:
        x = np.zeros(N)
        i = W-1 ;# start at bottom:
        while i >= 0:

            xi = (v[i] - np.sum(x*M[i,:]))/M[i,i]
            x[i] = xi
            i += -1
        
        # check if solution exists:
        x_nans = np.isnan(x) 
        nan_TF = x_nans.any()          # check if any elements are nan
        if nan_TF == True:
            if Print == True:
                print('....system not solvable...')
            return ('NA',np.nan*x)
        return ('independent', x) 
    
    
    # ---------------  Dependence:   
    if len(DEP) !=0:
        n_DEP = len(DEP)
        print(f'...{n_DEP} dependent variables detected: k = {DEP}...')
        i = 0; 
        while i < n_DEP:
            k = int(DEP[i]) ; # dependent variable index
            x = np.zeros(N) ; 
            s = N-1 # start at bottom ; note that gaussian elim
            # guaranteed upper diagonal, so s=W- 1 is bottom
            while s >= 0:
                if (DEP==s).any() == False:
                    x[s] = (v[s]-np.sum(x*M[s,:]))/M[s,s]
                if (DEP==s).any() == True: 
                    if v[s] != 0: # No solution
                        if Print == True:
                            print('....[solve] No Solution!...')
                        return ('NA',x*np.nan)
                    if s == k: # solve for dependent variable with Mii=1
                        x[s] = 1
                    if s !=k : # set other dependent variables to zero
                        x[k] = 0 #already set, but doen't hurt.
                       
                s += -1
            if i  == 0:
                X = x
            if i != 0:
                X = np.vstack([X,x])
            i +=1
            
            
        return ('dependent', X)
                    
                    



A0 = np.matrix(' 0 1   0  0 -1 -1 ;\
               -3 8   5  5  2 -2 ;\
               1  0  -1  0 -1  0 ;\
               4 -10 -7 -6 -3  3 ;\
               -1 3   2  2  2 -1 ;\
               0  0   0  0  0  0')










