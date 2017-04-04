'''A working function to generate prime numbers from 0 to n with asymptotic analysis in your public Github repo'''
def is_prime(N):
    for num in range(2,N+ 1):
       if num > 1:
           for i in range(2,num):
               if num % i == 0:
                   break
           else:
               return num