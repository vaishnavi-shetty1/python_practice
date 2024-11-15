def DivExp(a,b):
  assert a>0,'Enter number more than 0'

  if b==0:
    raise ZeroDivisionError('b values should not be 0')
  else:
    c=a/b
    return c
  a=int(input('Enter the value for a:')
  b=int(input('Enter the value for b:')
  print(DivExp(a,b))
