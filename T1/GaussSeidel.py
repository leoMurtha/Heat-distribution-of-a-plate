import numpy as np

# Gets initial input x0
def initialX(A, b):
    n = len(b)
    x0 = np.zeros(n,float)
    for i in range(n):
      x0[i] = (b[i]/A[i,i])
        
    return x0

# Matrix A, vector b, initial input x, number of iterations t    
# Returns the x(t) aproximation of the solution via gauss seidel
def solve(A, b, xi, t):
    # Using the formula x(k+1) = Cx(k) + g
    # where C = -L^-1*R and g L^-1*b
    # C = np.dot(np.linalg.inv(-L), np.dot(R, x))
    # g = np.dot(np.linalg.inv(L,b))
    # We can make a reduced formula
    # x = np.dot(np.linalg.inv(L), b -Rx)

    L = np.tril(A)
    R = np.triu(A, k = 1)
    x = xi.copy()
    invL = np.linalg.inv(L)
    
    for k in range(t): x = np.dot(invL, b - np.dot(R, x))
    
    return x    

