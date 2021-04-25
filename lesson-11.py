'''---------------Lesson 11-------------'''
yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    price = 0
elif yosh<=12: # 5,6,7,8,9,10,11,12 [5:12]
    price = 5000
elif yosh<=18: # 13,14,15,16,17, 18 [13,18]
  price = 7000
else:         # [18:]
    price = 10000
    
# print(f"Sizga kirish {price} so'm")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4: # yosh bolalarga bepul
#     price = 0
# elif yosh<=12: # 5 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh<65: # 13 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# else: # qariyalarga esa 8000 so'm
#     price = 8000
# print(f"Sizga kirish {price} so'm")

# my_num = 5
# user_son = int(input("Men o'ylagan sonni toping: "))
# if my_num == user_son:
#   print("Topdingiz!!!")
# elif my_num<user_son:
#   print("Sal kichraytiring!")  
# else:
#   print("Sal kattalashtiring!")  

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000    
# print(f"Sizga kirish {price} so'm")

# user_name = input('Ismingizni kiriting: >>> ').title()
# group_name = input('Gruppaingizni kiriting: >>> ').upper()

# rektor_jiyani = 'Axror'
# group = 'BET80'

# '''
# if SHART1==True and SHART2==True:
#   CMD1
# '''

# if (user_name == rektor_jiyani and group_name == group):
#   baho = 100
# else:
#   baho = 80
# print(f'Sizning bahoingiz {baho} !')

# kun = input("Bugun nima kun?>>> ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# temp = float(input("Temperaturangizni kirgizin:>>> "))
# hid = input("Hid sezyapsizmi? >>> ").lower()
# if temp>36.6 and (hid == "yo'q" or hid == 'yoq'):
#   print("Siz koronovirus bilan kasallangansiz!")
# elif temp>36.6 and hid == "ha":
#   print("Siz shamollagansiz!")
# else:
#   print("Siz sog'lomsiz!")  


# kun = input("Bugun nima kun? >>> ")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' or kun.lower() == 'shanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' or kun.lower() == 'shanba' and harorat<30:
#     print("Uyda dam olamiz!")
# else:
#   print('Oqishga yoqol!!!')
  
'''------------------11-AMALIYOT--------------------------------'''
# print("1-MASHQ")
'''Madinaga ex1. comments:
Songa toq son berganimda <Bu juft son emas deb chiqishi kerak edi!!!> son%2 da chiqqan natijani hech nima bilan solishtirmapsanku! HINT: son%2 > X  son%2==X  son%2 < X'''
# son = float(input("Juft son kiriting >>> "))
# if son%2 == 0:
#   print('Rahmat!')
# else:
#   print('Juft son kiriting')
# print("2-MASHQ")
'''Madinaga ex2. comments: Good Job!!!'''
# yosh = int(input("Yoshingiz nechida? >>> "))
# if yosh<=4 or yosh>=60:
#   print("Bepul")
# elif yosh<18:
#   print("10000 so'm") 
# else:
#   print("20000 so'm")   
# print("3-MASHQ")
# son1 =float(input("1-sonni kiriting: "))
# son2 = float(input("2-sonni kiriting: "))
# if son1>son2:
#   print(f'{son1}>{son2}')
# elif son1<son2:
#   print(f'{son1}<{son2}')  
# else:xz
#   print(f'{son1}={son2}')
# print('4-MASHQ')   
# mahsulotlar = ['olma', 'tarvuz', 'qovun', 'shaftoli', 'olcha', 'banan', 'gilos', 'anor', 'uzum', 'kivi']
# savat = []
# for n in range(5):
#   savat.append(input(f"Savatga {n+1} - mahsulotni qo'shing: "))
# for n in savat:
  # if n in mahsulotlar:
  #   print(f"Do'konimizda {n} bor")
  # else:
  #   print(f"Do'konimizda {n} yo'q")  
# print("5-MASHQ")
# mahsulotlar = ['olma', 'tarvuz', 'qovun', 'shaftoli', 'olcha', 'banan', 'gilos', 'anor', 'uzum', 'kivi']
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(5):
#   mahsulot = input(f"Savatga {n+1}- mahsulotni kiriting: ")
#   if mahsulot in mahsulotlar:
#     # print("Siz so'ragan mahsulotlar do'konimizda bor")
#     bor_mahsulotlar.append(mahsulot)
#   else:
#     # print("Quyidagi mahsulotlar yo'q: ") 
#     mavjud_emas.append(mahsulot)
# print("Quyidagi mahsulotlar yo'q: ")
# for x in mavjud_emas:
#   print(x)
# print("6-MASHQ") 
# foydalanuvchilar = ['Elik', 'Shalola', 'Kamola', 'Sumkachaqiz', 'Lola']
# login = input('Yangi login kiriting: ').title()
# if login in foydalanuvchilar:
#   print("Login band, yangi login tanlang!") 
# else:
#   print(f"Xush kelibsiz, {login}!")
# print('7-MASHQ')
# son = int(input("Istalgan son kiriting: "))
# for n in range(2,11):
#   if not son%n:
#     print(f"{son} soni {n} ga qoldiqsiz bo'linadi")


  
  

     


  


  

