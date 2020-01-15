def prime_gen(lim):
  """
  Takes integer lim and returns list of all primes below lim
  """
  sqrt_lim = lim**0.5
  #creates set of all odd digits below lim
  P = set([2]+list(range(3,lim,2)))
  n = 3
  #loop through all numbers less than sqrt of lim
  while n < sqrt_lim:
    if n in P: #if prime
      P -= set(range(2*n,lim,n)) #remove all multiples
    n += 1
  return P
