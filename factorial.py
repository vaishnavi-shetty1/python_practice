def factorial(n):
  fact=1
  for i in range (1,n+1):
    fact*=i
    return(fact)
n=int(input("Enter n:"))
n_fact=factorial(n)
r=int(input("Enter the value for r:"))
r_fact=factorial(r)
diff_fact=factorial((n-r))
bin-coeff=(n_fact)/(r_fact*(diff_fact))
print(round(bin_coeff,3))
