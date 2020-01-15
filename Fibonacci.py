fibonacci = {}
def fib_n(n):
  """
  Function that takes integer n and returns the n:th Fibonacci number
  """
  if n == 1 or n == 2:
    return 1
  if not n in fibonacci:
    a,b = fib_n((n+1)//2-1),fib_n((n+1)//2)
    if n%2==0:
      fibonacci[n] = b*(2*a + b)
    else:
      fibonacci[n] = a**2+b**2
  return fibonacci[n]

def fib_gen_k(s):
  """
  Function that takes integer of stepsize and returns coefficient of that stepsize
  """
  if s == 1:
    return 1
  else:
    a,b = 1,3
    for i in range(s-1):
      a,b = b,a+b
    return a

def fib_gen(count,steps=1):
  """
  Function that takes integers count and steps and returns a generator of a *count* long sequence for every *steps*th Fibonacci number
  """
  k = fib_gen_k(steps)
  sign = (-1)**(steps+1)
  a,b = 0,fib_n(steps)
  i = 1
  while i <= count:
    a,b = b,k*b+sign*a
    i += 1
    yield a


