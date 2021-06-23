# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# print("Do'konimizdagi mahsulotlar:")    
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# print(telefonlar.values())

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)

#     print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)

'''------------LESSON-15: Lug'ar elementlari bilan ishlash-------------'''
# key   : Value
# Eldor : Note8
# Elyor : OnePlus 
# Mom   : POCO
# Madina: Huawei 

### List da loop usullari
# nums = [11,12,13,14,15]
# for i in range(len(nums)): # index buyicha loop
#   print(i) # listning index print qilamiz: 0, 1, 2, 3 4
#   print(nums[i]) # listning osha orinda turgan qiymatini: 11, 12, 13, 14, 15

# for num in nums: # qiymati boyicha boyicha loop 
#   print(num)

### Dictionary da LOOP usullari
# family = {
#   'Eldor' : 'Note8',
#   'Elyor' : 'OnePlus', 
#   'Mom'   : 'POCO',
#   'Madina': 'Huawei'
#   } 

# print(family.items())
# for k, v in family.items():
#   print('key =', k)
#   print('value =', v)
# print('--------------------')

# print(family.keys()) #dict_keys(['Eldor', 'Elyor', 'Mom', 'Madina'])
# for k in family.keys():
#   print("key =", k)
# print('--------------------')

# print(family.values())
# for v in family.values():
#   print("Value =", v)
# print('--------------------')

# for member in family: # family = family.keys()
#   print('something =', member) 

'''
Masala-1: family dict dan memebers degan [] va phones degan [] hosil qiling. 
'''
# members = []
# phones = []

# # for k in family.keys():
# #   members.append(k)

# # for v in family.values():
# #   phones.append(v)
    
# for k, v in family.items():
#   members.append(k)
#   phones.append(v)

# print('members =', members)
# print('Phones =', phones)  

'''
Masala-2:
{
  'olma':10000,
  'anor':20000,
  'uzum':40000,
  'anjir':25000,
  'shaftoli':30000
}
Kalitlarni tartiblangan holda console ga chiqaring.
'''
# mahsulotlar = { 
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# x = mahsulotlar.keys()    
# print('x =', x)
# print('x ing turi =', type(x))
# y = sorted(x)
# print('y =', y)
# print('y ning turi =', type(y))


# for k in sorted( mahsulotlar.keys() ):
#   print(k)
 

'''
Masala-3:
{
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
nechi xil telefon lug'atda mavjud?    
'''

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }

# tellar = []
# for v in set(telefonlar.values()):
#   tellar.append(v)
# print(tellar)


