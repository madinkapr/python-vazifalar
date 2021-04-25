'''-----for loop ustida amallar----'''

sonlar = [1,3,2,5,4,67,87,63,100,12,60,44,25]
result1 = []
result2 = []
result3 = []
## 1-usul: qiymati bo'yicha
for son in sonlar:
  result1.append(son)

print(result1)

## 2-usul: index bo'yicha
for i in range(len(sonlar)):
  result2.append(sonlar[i])

print(result2)

''''
EX-1: [1,3,2,5,4,67,87,63,100,12,60,44,25] -> [2,5,4,67,87,63,100,12,60]
'''
for i in range(2, len(sonlar)-2):
  result3.append(sonlar[i])
print(result3)
'''
EX-2: [1,3,2,5,4,67,87,63,100,12,60,44,25] da toq o'rinda turgan sonlarni console ga chiqaring.
'''
sonlar = [1,3,2,5,4,67,87,63,100,12,60,44,25]
result4 =[]
for i in range(len(sonlar)):
  if i%2 !=0:
    result4.append(sonlar[i])
print(result4)