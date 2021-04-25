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
# sonlar = [4,3,56,32,73,12,125] #  bu yerda son emas sonlar. p
# for son in sonlar:
#   if son%2==0:
#     print(son)

# print('MASHQ-7: [14,13,156,232,733,123,125] larning ichidan faqat juftlarini consolga chiqaring.')
# sonlar = [14,13,156,232,733,123,125]
# for son in sonlar:
#   if son%2==0:
#     print(son)

# print('MASHQ-8*: [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200] ichida ikki xonalilarni song esa uch xonali sonlarni consolga chiqaring.')  
# sonlar = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# print('-------1-usul-------')
# for son in sonlar: 
#   if 10<=son<=99: # bu ikki xonami yoki yoqmi tek shirayaptida
#     print('2 xonali son:', son) # got it?yes
# for son in sonlar:
#   if 100<=son<=999:
#     print('3 xonali sonlar:', son)  
# # mana shu yerda 2ta loop da emas, 1ta loopda xal qila olasanmi? boldim
# print('-------2-usul-------')
# two = []
# three = []
# for son in sonlar: 
#   if 10<=son<=99:
#     two.append(son)
#   elif 100<=son<=999:
#     three.append(son)
# print(f'2-xonali sonlar: {two}') 
# print(f'3 xonali sonlar: {three}')
    

# print('MASHQ-9: [100, 200, 300, 400, 500] sonlarni kamayish tartibida console ga chiqaring.')
# nums = [100, 200, 300, 400, 500] # nums - sonlar, num - son
# # yangi_sonlar = sorted(nums, reverse=True) # 1-usul
# # print(yangi_sonlar) 
# nums.sort(reverse=True) # 2-usul
# print(nums) 

# # sorted(nums, reverse=False) da osish tartibida
# # sorted(nums, reverse=True) da kamayish tartibida chiqaradi
# # sorted(nums) degani sorted(nums, reverse=False) degani!

# print('MASHQ-9.1: [200, 400, 300, 4000, 50] sonlarini quyidagi korinishda console ga chiqaring: \nosish:[50,200,300,400,4000]\nkamayish:[4000,400,300,200,50]\noriginal: [200, 400, 300, 4000, 50]')
# print('-------------------------')
# orginal = [200, 400, 300, 4000, 50]
# osish = sorted(orginal)
# print(f'Osish: {osish}')
# kamayish = sorted(orginal, reverse=True)
# print(f'Kamayish: {kamayish}')
# print(f'Orginal: {orginal}')


# print('MASHQ-10: [1, 2, 3, 4, 5, 6, 7] listning har bir elementini kvadratga oshirib [1,4,9,16,25,36,49] ga aylantirib consolega chiqaring.')
# # orig: [....]
# # kvdt: [....]
# kvdt = []
# sonlar = [1, 2, 3, 4, 5, 6, 7] 
# for son in sonlar:
#   kvdt.append(son**2)
# print('orig:', sonlar)
# print('kvdt:', kvdt)  

# MASHQ-11: [100, 89, 88, 95, 90, 75, 100, 56] fanlardan bohalar royxati berilgan bolsa, studentning ortacha bahosini console ga chiqaring.
baholar = [100, 89, 88, 95, 90, 75, 100, 56]
## 1-usul:
# summa = 0
# for baho in baholar:
#   summa = summa + baho # 1: summa = 0 + 100 = 100
#                        # 2: summa = 100 + 89 = 189
#                        # 3: summa = 189 + 88 = 277
# avg = summa / len(baholar)
# print(avg)

## 2-usul:
summa = sum(baholar)
avg = summa/len(baholar)
print(avg)

 