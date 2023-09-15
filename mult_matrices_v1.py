import numpy as np

def multiply(A, B, C):
    N=len(A)
    for i in range(N):
      for j in range(N):
        C[i][j] = 0
        for k in range(N):
          C[i][j] += A[i][k] * B[k][j]


if __name__=='__main__':
    A = np.random.randint(-10, 10, (2000, 2000))
    print(f'A={A}')
    B = A
    print(f'B={B}')
    n = len(A)
    C = np.zeros((n, n))
    multiply(A, B, C)
    print(f'C={C}')
    print('Changing B')
    B = np.random.randint(-10, 10, (2000, 2000))
    print(f'B={B}')

    multiply(A, B, C)
    print(f'C={C}')