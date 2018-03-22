# Dada uma placa quadrada 1x1 m^2 e as temperaturas de fronteiras
# calcule a temperatura nesta placa e visualize a distribuição
# usando Gauss-Seidel e um grid nxn
import GaussSeidel as gsd
import numpy as np

# Retorna a matriz de coeficientes e o vetor B
def createLinearSystem(grid, n):
    m = (n-2)**2
    A = 4*np.identity(m, float) # Vezes quatro pois a variavel é a média entre 4
    b = np.zeros(m, float)
    
    for i in range(1, n-1):
        for j in range(1,n-1):
            g = 0
            #print('{} {} {} {}'.format(grid[i,j-1], grid[i-1,j], grid[i,j+1], grid[i+1,j]))
            
            if(grid[i,j-1] == 3.14):
                A[(i-1)*(n-2) + (j-1)][(i-1)*(n-2) + (j-2)] = -1
                #print('{} = {} {}'.format(((i-1)*(n-2) + (j-1)),i-1, (i-1)*(n-2) + (j-2)))
            else: g = g + grid[i, j-1]
            
            if(grid[i-1,j] == 3.14):
                A[(i-1)*(n-2) + (j-1)][(i-2)*(n-2) + (j-1)] = -1
                #print('{} = {} {}'.format(((i-1)*(n-2) + (j-1)),i-1, (i-2)*(n-2) + (j-1)))
            else: g = g + grid[i-1, j]
            
            if(grid[i,j+1] == 3.14):
                A[(i-1)*(n-2) + (j-1)][(i-1)*(n-2) + j] = -1
                #print('{} = {} {}'.format(((i-1)*(n-2) + (j-1)),i-1, (i-1)*(n-2) + j))
            else: g = g + grid[i, j+1]
            
            if(grid[i+1,j] == 3.14):
                A[(i-1)*(n-2) + (j-1)][i*(n-2) + ((j)-1)] = -1
                #print('{} = {} {}'.format(((i-1)*(n-2) + (j-1)),i-1, i*(n-2) + ((j)-1)))
            else: g = g + grid[i+1, j]    
            
            b[(i-1)*(n-2) + (j-1)] = g
            
    return A, b       
 
def initGrid(dR, n):
    grid = np.full((n, n), float(3.14),float)
    
    print('>>Inicializando o grid.')
    for i in range(n):
        grid[i,0] = dR[0] # Parte esquerda
        grid[0,i] = dR[1] # Parte do topo
        grid[i,n-1] = dR[2] # Parte direita
        grid[n-1,i] = dR[3] # Parde de baixo
    
    return grid
        
def main():

    print('>>>A coleta de fronteira é sentido horário começando pelo lado esquerdo.')
    print('>>>Lembrando que a dimensão do grid é n gera (n-2)^2 variaveis.')
    n = int(input('>>>Digite a dimensão do grid.\n'))
    dR = np.zeros(4) # Vetor de temperaturas das fronteiras
    
    for i in range(4):
        dR[i] = float(input('>>>Digite a temp da fronteira [{}].\n'.format(i+1)))
    
    grid = initGrid(dR, n)    
    A, b = createLinearSystem(grid, n) 
    #print(gsd.solve(A,b,x,n))

if __name__ == "__main__":
    main()