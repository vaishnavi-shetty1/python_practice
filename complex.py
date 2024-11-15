class Complex:
  summ=0j
  def add_comp(self,comp):
    self.summ+=comp
c=Complex()
n=int(input('Enter the number of values:'))
if n>=2:
  i=1
  while i<=n:
    numb=eval(input('Enter the complex number:'))
c.add_comp(numb)
i+=1
print(c.summ)
else:
print('Enter n greater than 1 or equal to 2')
