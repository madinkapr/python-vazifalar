''' ######################### 10 IF-ELSE ########################### '''

# yosh_madina = 19
# yosh_lobar = 20

# if yosh_madina > yosh_lobar:
#   print('Madinaning singlisi Lobar')
# elif yosh_madina == yosh_lobar:
#   print('Madinaning dosti Lobar')
# else:
#   print('Madinaning opasi Lobar')

# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar:
#   if avto == 'bmw':
#     print(avto.upper())
#   else:
#     print(avto.title())

# ism = 'Ali'

# print(ism == 'ali')
# print(ism == 'Ali')
# print(ism == 'Vali')


# ism = input("Ismingiz nima?\n")

# if ism.lower() == 'ali':
#   print(f'Xush kelibsiz, {ism.title()}')
# else:
#   print(f'Kechirasiz {ism.title()}, siz bizning klub azosi emassiz')


# rektor_jiyanlari = ['AXrol', 'zulfiya', 'Sobir']

# ism = input('Ismingizni kiriting!\n')
# jiyan_topdingmi = False
# for jiyan in rektor_jiyanlari: # user kiritgan ism jiyanlari listida bormi?
#   if ism.lower() == jiyan.lower():
#     jiyan_topdingmi = True

# if jiyan_topdingmi == True:
#   print('Sizning bahoingiz 100%')
# else:
#   print('Sizning bahoingiz 89%')

# # javobingiz = int(input('2x15 nechi boladi?\n'))
# javobingiz = input('2x15 nechi boladi?\n')
# if int(javobingiz) == 30:
#   print('Topdingiz! Qarsak....')
# else:
#   print('Ikkichi, shuni ham bilmaysanmi, tupoy!')


# yosh = input('Yoshingiz nechida?\n')
# if yosh >= '18':
#   print('Xush kelibsiz kinoteatrga!')
# else: 
#   print('Sizga kirish mumkinmas!')


# login = input('Yangi login kiriting!\n')

# if len(login) < 5:
#   print(f'Login uzunligi 5dan uzunroq bolishi kerak. Sizning loginingizning uzunligi {len(login)}')

# # Madinaning usuli
# yili = int(input("Nechinchi yilda tug'ilgansiz?\n"))
# yosh = 2021 - yili
# if yosh > 0:
#   print(f"Yoshingiz {yosh} da!")  
# else:
#   print("Tug`ilgan yilingizni notog'ri kiritdingiz.")

  
# print(f"Yoshingiz {yosh} da!") if yosh > 0 else print("Tug`ilgan yilingizni notog'ri kiritdingiz.") 
 
# # Eldorning usuli
# yili = int(input("Nechinchi yilda tug'ilgansiz?\n"))
# if yili > 2021:
#   print("Tug`ilgan yilingizni notog'ri kiritdingiz.")
# else:
#   yosh = 2021 - yili
#   print(f'Siz {yosh} da!')


'''#######BIR QATOR if/else #######'''
# yosh = int(input("Yoshingiz nechida?>>> "))
# if yosh > 18: print('Kinoga marhamat!')

# if yosh > 18:
#   print('Kinoga marhamat!')
#   print(f'Siz {65-yosh} yildsan keyin pensiyaga chiqasiz!')


# x = 12
# y = 25
# x, y = 12, 25

# if x>y: # SHART
#   print('x>y') # commanda1
# else:   
#   print('x<y') # commanda2

# print('x>y') if x>y else print('x<y')

####commanda1 if SHART else commanda2#####
# yosh = int(input("Yoshingizni kiriting!\n"))

# if yosh >= 18:
#   print('Kinoga marhamat!') # commanda1
# else:
#   print('Kinoga kirish mumkin emas!') # commanda2

# print('Kinoga marhamat!') if yosh >= 18 else print("Kinoga kirish mumkinmas!")


'''###### TENG EMAS SHARTI  ######'''

# 12 != 13
# 'Avaz' != 'avaz'
# 3.14 != 3.1

# rektor_jiyanlari = ['Axrol', 'Zulpiya', 'Sobir']

# ism = input('Ismingizni kiriting!\n')

# for jiyan in rektor_jiyanlari:
#   if jiyan != ism:
#     print('Sizning bohoingiz 85%')
#   else:
#     print('Sizning bohingiz 100%')

# jiyan_bormi = False
# for jiyan in rektor_jiyanlari:
#   if jiyan.lower() == ism.lower(): jiyan_bormi = True

# print('Sizning bohoingiz 85%') if jiyan_bormi != False else print('Sizning bohingiz 100%')


'''----------------AMALIYOT--------------'''
# print("1-MASHQ")
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car == 'gm':
#     print(car.upper())
#   else:
#     print(car.title())

# print("2-MASHQ")
# for car in cars:
#   if car != 'gm':
#     print(car.title())
#   else:
#     print(car.upper())

# print("3-MASHQ")
# ism = input("Ismingiz nima?\n")
# if ism.lower() == 'admin':
#   print("Xush kelibsiz, Admin.Foydalanuvchilar ro'yxatini ko'rasizmi?") 
# else:
#   print(f"Xush kelibsiz, {ism}!")

# print("4-MASHQ")
# son1 = input("Birinchi sonni kiriting!\n")
# son2 = input("Ikkinchi sonni kiriting!\n")
# if son1 == son2:
#   print("Sonlar teng")

# print("5-MASHQ")
# son = int(input("Istalgan son kiriting!\n"))
# if son < 0:
#   print("Manfiy son")
# else:
#   print("Musbat son")

print("6-MASHQ")
son = int(input("Son kiriting!\n"))
if son > 0:
  print(son**(1/2))
else:
  print("Musbat son kiriting!")