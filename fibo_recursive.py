# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

if __name__ == '__main__':
    for x in range(0,9):
        y = recur_fibo(x)
        print(y)