'''---------QAYTARISH [1~12] lessonlar--------'''
# print('MASHQ-1: 1 dan 10 bolgan sonlarni consolega chiqaring')
# for n in range(1,11):
#   print(n)

# print('MASHQ-2: bir xonali barcha juft sonlarni condolga chiqaring')
# for n in range(2,10,2):
#   print(n)

# print('MASHQ-3: bir xonali barcha toq sonlarni condolga chiqaring')
# for n in range(1,10,2):
#   print(n)

# print('MASHQ-4: ikki xonali barcha juft sonlarni condolga chiqaring')
# for n in range(10,100,2):
#   print(n)

# print('MASHQ-5: ikki xonali barcha toq sonlarni condolga chiqaring')
# for n in range(11,100,2):
#   print(n)
  
# print('MASHQ-6: [4,3,56,32,73,12,125] larning ichidan faqat juftlarini consolga chiqaring.')
# list1 = [4,3,56,32,73,12,125]
# for n in list1:
#   if n%2 == 0:
#     print(n)

# print('MASHQ-7: [14,13,156,232,733,123,125] larning ichidan faqat juftlarini consolga chiqaring.')
# list2 = [14,13,156,232,733,123,125]
# for n in list2:
#   if n%2 == 0:
#     print(n)

# print('MASHQ-8*: [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200] ichida ikki xonalilarni song esa uch xonali sonlarni consolga chiqaring.')
# # list3 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# list3 = [182, 515, 32, 42, 545, 75, 22, 132, 15, 180, 20]
# print("2xonali sonlar: ")
# for n in list3:
#   if 10<=n<=99:
#     print(n)
# print("3xonali sonlar: ")
# for n in list3:
#   if 100<=n<=999:
#     print(n)

# for n in list3:
#   if 10<=n<=99:
#     print('2-xonali son:', n)
#   elif 100<=n<=999:
#     print('3-xonali sonlar:', n) 
  

# print('MASHQ-9: [100, 200, 300, 400, 500] sonlarni kamayish tartibida console ga chiqaring.')
# list1 = [100, 200, 300, 400, 500]
# # 1-Ususl:
# # range(start, end, step)
# for i in range(len(list1)-1,-1,-1):
#   print(list1[i])

# # 2-usul: hint sorted()
# list2 = sorted(list1, reverse = True)
# print('list2 =', list2)
   

print('MASHQ-10: [1, 2, 3, 4, 5, 6, 7] listning har bir elementini kvadratga oshirib [1,4,9,16,25,36,49] ga aylantirib consolega chiqaring.')
list1 = [1, 2, 3, 4, 5, 6, 7] 
list2 = []
for n in list1:
  list2.append(n**2)
print(list2)  
 