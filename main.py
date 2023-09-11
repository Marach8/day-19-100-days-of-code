print('Loan Calculator!')
print()
print('$1000 for 10 years at 5% APR.')
print()
p = 1000
for t in range(1,11):
  r = 0.05
  p += (p*r)
  print(f'Year{t} is ${round(p,2)}')
print()
print(f'You owe ${round((p-1000), 2)} interest!')