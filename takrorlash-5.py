'''Takrorlash-5'''

print("Ex1: \n[23,12,2,43,4,56,7,45,66,745,66,44,33,765,43,98] sonlarda toq o'rinda turganlarining kopaytmasini toping.")
sonlar = [23,12,2,43,4,56,7,45,66,745,66,44,33,765,43,98]
kopaytma = 1
for i in range(len(sonlar)):
  if i%2 != 0:
    kopaytma = kopaytma * sonlar[i]
print(kopaytma)   

print("\nEx2: \n[23,12,2,43,4,56,7,45,66,745,66,44,33,765,43,98] sonlarda juft o'rinda turganlarining yig'indisini toping.")
# sonlar = [23,12,2,43,4,56,7,45,66,745,66,44,33,765,43,98]
yigindi = 0
for i in range(len(sonlar)):
  if i%2 == 0:
    yigindi = yigindi + sonlar[i]
print(yigindi)

print("\nEx3: \n[23,12,2,43,4,56,7,45,66,745,66,44,33,765,43,98] sonlarda toq sonlarining kopaytmasini toping.")
kopaytma = 1
for son in sonlar:
  if son%2 != 0:
    # kopaytma = kopaytma * son
    kopaytma *= son
print(kopaytma) 
print(23*43*7*45*745*33*765*43)


print("\nEx4: \n[23,12,2,43,4,56,7,45,66,745,66,44,33,765,43,98] sonlarda juft sonlarining yig'indisini toping.")
yigindi = 0
for son in sonlar:
  if son%2 == 0:
    # yigindi = yigindi + son
    yigindi += son
print(yigindi) 
print(12+2+4+56+66+66+44+98)

