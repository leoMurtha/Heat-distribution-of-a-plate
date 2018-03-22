# Dada uma placa quadrada 1x1 m^2 e as temperaturas de fronteiras
# calcule a temperatura nesta placa e visualize a distribuição
# usando Gauss-Seidel e um grid nxn

# Aluno: Leonardo Meireles Murtha Oliveira
# NºUSP: 4182085
 
import GaussSeidel as gsd
import numpy as np
import matplotlib.pyplot as plt

# Retorna a matriz de coeficientes e o vetor B
def createLinearSystem(grid, n):
    m = (n-2)**2
    A = 4*np.identity(m, float) # Vezes quatro pois a variavel é a média entre 4
    b = np.zeros(m, float)
    
    for i in range(1, n-1):
        for j in range(1,n-1):
            g = 0
            
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

# Inicializa o grid com as temp. fronteiras
def initGrid(dR, n):
    grid = np.full((n, n), float(3.14),float)
    
    print('>>Inicializando o grid.')
    grid[0,0] = (dR[0] + dR[1])/2
    grid[n-1,0] = (dR[1] + dR[2])/2
    grid[n-1,n-1] = (dR[2] + dR[3])/2
    grid[0, n-1] = (dR[3] + dR[0])/2
    
    for i in range(1,n-1):
        grid[i,0] = dR[0] # Parte esquerda
        grid[0,i] = dR[1] # Parte do topo
        grid[i,n-1] = dR[2] # Parte direita
        grid[n-1,i] = dR[3] # Parde de baixo
    
    return grid

# Atualiza o grid com a solução
def updateGrid(grid, xf, n):
    for i in range(1, n-1):
        for j in range(1,n-1):
            grid[i][j] = xf[(i-1)*(n-2) + (j-1)]
            
def main():

    print('>>>A coleta de fronteira é sentido horário começando pelo lado esquerdo.')
    print('>>>Lembrando que a dimensão do grid é n gera (n-2)^2 variaveis.')
    n = int(input('>>>Digite a dimensão do grid.\n'))
    dR = np.zeros(4) # Vetor de temperaturas das fronteiras
    
    for i in range(4):
        dR[i] = float(input('>>>Digite a temp da fronteira [{}].\n'.format(i+1)))
    
    grid = initGrid(dR, n) # Inicia o grid com as temperatura de fronteiras em equilibrio   
    A, b = createLinearSystem(grid, n)  # Cria a matriz a partir das equações
    xi = gsd.initialX(A, b) # Pega o chute inicial
    t = 20 # Número de iterações do Gauss-Seidel
    xf = gsd.solve(A, b, xi, t) # Resolve o sistema
    updateGrid(grid, xf, n) # Atualiza o grid com a solução aproximada
    
    # Parte de visualização
    plt.title('Heat Distribution')
    plt.xlabel('Coluna do grid')
    plt.ylabel('Linha do grid')
    plt.imshow(grid, cmap='plasma', interpolation='nearest')
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    main()