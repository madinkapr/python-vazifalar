''' Lesson-8: RO'YXATLAR BILAN ISHLASH '''

########## SORT() metodi/funksiyasi ############

# numbers1 = [4,3,5,7,9,1,8]
# print("Numbers1 Before =", numbers1)
# numbers1.sort() # O'sish tartibida sortirovka
# print("Numbers1 After =", numbers1)

# numbers2 = [3,4,1,5,7,14,1,80]
# print("Numbers2 Before =", numbers2)
# numbers2.sort(reverse=True) # Kamayish tartibida sortirovka
# print("Numbers2 After =", numbers2)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi', 'alfa rameo']
# print("Cars before =", cars)
# cars.sort(reverse=True)
# print("Cars after =", cars)

# ismlar = ['Madinabonu', 'Alisher', 'Qayum', 'Ixtiyor', 'anvar']
# print("Ismlar before =", ismlar)
# ismlar.sort()
# print("Ismlar after =", ismlar)

########## SORTED() metodi/funksiyasi ############
# sonlar = [3,2,5,3,1,4,2,7,3]
# print("Before sonlar: ", sonlar)
# new_sonlar = sorted(sonlar)
# # print("tartibsis sonlar =", sonlar, "\ntartibli sonlar =", new_sonlar)
# # print("tartibsiz sonlar:  ", sonlar)
# print("tartiblanga sonlar:", new_sonlar)


# sariq_xamyon = [500, 100, 1000]
# # sariq_xamyon.sort()
# # print("Pullarizni taxlab berdim:", sariq_xamyon)
# qizil_xamyon = sorted(sariq_xamyon)
# print("Mana sizning sariq xamyoningiz, tegmadim bunga:", sariq_xamyon)
# print("Qizil kashelyokka pullarizni taxlab quydim, mana:", qizil_xamyon)
# print("Qizil kashelyokka pullarizni taxlab quydim, mana:", sorted(sariq_xamyon))


######## REVERSE() FUNKSIYA/METOD ####################
# ''' Ro'yxatni teskarisiga yozadi '''
# pullar = [500,100,1000]
# pullar.reverse()
# print(pullar)

# mevalar = ['olma', 'anor', 'shaftoli', 'apelsin']
# mevalar.reverse()
# print(mevalar)

###### Ro'yxatning uzunligi LEN() ######
# mevalar = ['olma', 'anor', 'shaftoli', 'apelsin']
# mevalar_soni = len(mevalar) # len() -- Length-uzunlik
# print(mevalar_soni, "xil mevalar berilgan")

# cars = ["spark", "malibu", "lacetti", "nexia", "damas", "cobalt", "matiz", "tico", "captiva"]
# cars_soni = len(cars)
# print("O`zbekistonda", cars_soni, "xil mashina ishlab chiqariladi")


########## RANGE Funksiysi #############
# print(list(range(0,3)))   # [a,b) -->[0,3)-->0,1,2
# print(list(range(5,15)))
# bir_xonali = list(range(0,10))
# ikki_xonali = list(range(10,100))
# print("Bir xonali sonlar =", bir_xonali)
# print("Ikki xonali sonlar =", ikki_xonali)
# # range(start, end, step) 
# test = list(range(0, 10, 2))
# print(f"test = {test}")

# = {juft_sonlar}")
# juft_sonlar = list(range(2,10,2))
# print(f"Bir xonali juft sonlar = {juft_sonlar}")
# juft_sonlar = list(range(10,100,2))
# print(f"Ikki xonali juft sonlar = {juft_sonlar}" ) 
# toq_sonlar = list(range(1,10,2))
# print(f"Bir xonali toq sonlar = {toq_sonlar}")
# toq_sonlar = list(range(11,100,2))
# print(f"Ikki xonali toq sonlar = {toq_sonlar}")

# # 100 dan katta bo'lmagan barcha 3ga karrali sonlarni chqaring
# uch_karrali = list(range(3,100,3))
# print("3ga karrali sonlar =", uch_karrali)

# teskari_sonlar = list(range(20, 0, -5))
# print(f"teskari tartib sonlar = {teskari_sonlar}")





# ###########Amaliyot###########
# # 1.O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# print("SHART-1: O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring")
# davlat = ['Xitoy', 'Koreya', 'Amerika', 'Avstraliya','Germaniya']
# print(davlat)

# # 2.Ro'yxatning uzunligini konsolga chiqaring
# print("SHART-2: Ro'yxatning uzunligini konsolga chiqaring")
# davlatlar_soni = len(davlat)
# print("Davlatlar soni =", davlatlar_soni)

# # 3.sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print("SHART-3: sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring")
# davlatlar = sorted(davlat)
# print(davlatlar)             

# # 4.sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print("SHART-4: sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring")
# davlatlar = sorted(davlat, reverse = True) # good!
# print(davlatlar) # 4-vazifani tog'ri ishlading!

# # 5.Asl ro'yxatni qaytadan konsolga chiqaring
# print("SHART-5: Asl ro'yxatni qaytadan konsolga chiqaring")
# print(davlat) ## GOOD JOB!
 

# # 6. reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# print("SHART-6: reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring")
# davlat.reverse()
# print(davlat)

# # 7.sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# print("SHART-7a: sort() metodi yordamida ro'yxatni avval alifbo bo'yicha konsolga chiqaring.")
# davlat.sort()
# print(davlat)
# print("SHART-7b: sort() metodi yordamida ro'yxatni alifboga teskari tartibda konsolga chiqaring.") 
# davlat.sort(reverse=True) # NICE!
# print(davlat)


# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# print("SHART-8: 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing")
# juft_sonlar = list(range(120,1200,2)) 

''' ---------RO'YXATNI KESISH--------- '''
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[1:4]
# print('Mening moshinalarim =', my_cars)

# my_cars = cars[:4]
# print(my_cars)

# my_cars = cars[4:]
# print(my_cars)


''' ------------RO'YXATDAN NUSXA OLISH---------- '''
# sonlar = [1,2,3,4,5]
# sonlar2 = sonlar # FF32
# print('sonlar =', sonlar)
# print('sonlar2 =', sonlar2)
# print('===================')
# sonlar2.append(6)
# sonlar2.append(7)
# print('sonlar =', sonlar)
# print('sonlar2 =', sonlar2)

# sonlar = [1,2,3,4,5] # FF32
# sonlar2 = sonlar[:] # FF32->FF35

''' -----------TUPLES O'ZGARMAS RO'YXAT---------- '''
# boholar = (5, 3, 5)
# boholar = list(boholar)
# boholar[1] = 4
# boholar = tuple(boholar)
# print(boholar)

# boholar.append(10)
# print(boholar)
#---------------Amaliyot------------
# #1. O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# print("1-mashq:O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring:")
# davlatlar = ["Turkiya", "Korea", "Germaniya", "Avstriya"]
# print('Dastlabki davlatlar =', davlatlar)
# # 2.Ro'yxatning uzunligini konsolga chiqaringx = len(davlatlar)
# print("2-mashq:Ro'yxatning uzunligini konsolga chiqaring:")
# x = len(davlatlar)
# print("Ro'yhatda", x, "ta davlat bor")
# # 3.sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print("3-mashq:sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring:")
# sorted_davlatlar = sorted(davlatlar)
# print("Tartiblangan davlatlar =", sorted_davlatlar)
# # 4.sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print("4-mashq:sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring:")
# reverse_davlatlar = sorted(davlatlar, reverse=True)
# print("Teskari davlatlar =", reverse_davlatlar)
# # 5.Asl ro'yxatni qaytadan konsolga chiqaring
# print("5-mashq:Asl ro'yxatni qaytadan konsolga chiqaring:")
# print("asl davlatlar =", davlatlar)
# # 6.reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# print("6-mashq:reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring:")
# davlatlar.reverse()
# print(davlatlar)
# 7.sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# print("7-mashq:sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring:")
# davlatlar.sort()
# print("alifbo bo'yicha =", davlatlar)
# davlatlar.sort(reverse=True)
# print('Alifboga teskari =', davlatlar)


# 8.120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# print("8-mashq:120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing:")
# juft_sonlar = list(range(120, 1200, 2))
# print('Juft sonlar =', juft_sonlar)

# 9.Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print("9-mashq:Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring:")
# x = sum(juft_sonlar)
# print("yig`indisi =", x)

# 10.Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# print("10-mashq:Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring")
# eng_katta = max(juft_sonlar)
# eng_min = min(juft_sonlar)
# print("Eng katta va eng kichik son ayirmasi =", max(juft_sonlar)-min(juft_sonlar))

# 11.Ro'yxatdagi elementlar sonini hisoblang
# print("11-mashq:Ro'yxatdagi elementlar sonini hisoblang:")
# elementlar_soni = len(juft_sonlar)
# print("Elementlar soni =", elementlar_soni)

# '''12.Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring'''
# print("12-mashq:Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring:")
# x = len(juft_sonlar)
# print("Ro`yhat uzunligi =", x)
# boshidan = juft_sonlar[0:20]
# print("Ro`yhat boshi =", boshidan)
# ortasi = juft_sonlar[270:290]
# print("Ro'yhat o'rtasi =", ortasi)
# oxiri = juft_sonlar[520:540]
# print("Ro'yhat oxiri =", oxiri)

'''13.taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting'''
print("13-mashq: Taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting")
taomlar = ["manti", "chuchvara", "osh", "somsa", "sho'rva", "lag'mon"]
print('Taomlar =', taomlar)

'''14. nonushta degan yangi ro'yxatga taomlardan nusxa oling''' 
print("14. nonushta degan yangi ro'yxatga taomlardan nusxa oling")
nonushta = taomlar[:]
print("Nonushta =", nonushta)

'''15-16. Yangi ro'yxatda faqat xamirli taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing'''
print("15-16. Yangi ro'yxatda faqat xamirli taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing")
nonushta.remove("osh")
nonushta.remove("sho'rva")
nonushta.append("norin")
nonushta.append("shilpildoq")
print("Taomlar =", taomlar)
print("Xamirli ovqatlar =", nonushta)

'''17. Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.'''
print("17. Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = <qaymoq va non> deb qiymat berib ko'ring.")
nonushta = tuple(nonushta) # list->tuple
nonushta = list(nonushta)  # tuple->list
nonushta[0] = "qaymoq va non"
nonushta.append(nonushta)
print(nonushta)



'''--------------------'''
# '''---------------------8-dars AMALIYOT-------------------'''
# print("1-MASHQ")
# davlatlar = ['Tashkent', 'Kanada', 'Korea', 'Singapur', 'Xitoy']
# print(davlatlar)
# print('2-MASHQ')
# print('Davlatlar soni:', len(davlatlar))
# print('3-MASHQ')
# davlat = sorted(davlatlar)
# print(davlat)
# print('4-MASHQ')
# print(sorted(davlatlar,reverse=True))
# print('5-MASHQ')
# print(davlatlar)
# print('6-MASHQ')
# davlatlar.reverse()
# print(davlatlar)
# print('7-MASHQ')
# davlatlar.sort()
# print(davlatlar)
# print(sorted(davlatlar,reverse=True))
# print('8-MASHQ')
# sonlar = list(range(120, 1202, 2))
# print('sonlar = ', list(range(120,1202,2))) 
# print('sonlar = ', sonlar) 
# print('9-MASHQ')
# print("Sonlar yig'indisi:", sum(list(range(120,1202,2))))
# print('10-MASHQ')
# qimmat = int(max(sonlar)) 
# arzon = int(min(sonlar))
# print('qimmat - arzon =', qimmat-arzon)
# print("qimmat = ", qimmat)
# print("arzon = ", arzon)
# print('11-MASHQ')
# print('sonlar elementi =', len(sonlar))
# print('12-MASHQ')
# boshidagi_son = sonlar[0:20]
# print('Beginner nums:', boshidagi_son)
# ortasidagi_son = sonlar[270:290]
# print('middle nums:', ortasidagi_son)
# end_son = sonlar[521:541]
# print("End nums:", end_son)
# print('13-14-MASHQ')
# taomlar = ['chuchvara', 'osh', 'xonim', 'manti', 'somsa']
# nonushta = taomlar
# print("Nonushta =", nonushta)
# print('15-MASHQ')
# nonushta.pop(0)
# print(nonushta)
# nonushta.pop(1)
# print(nonushta)
# nonushta.pop(1)
# print(nonushta)
# nonushta.pop(1)
# print("Yangi ro'yhat =", nonushta)
# nonushta.append('shirchoy')
# nonushta.append('kolbasa')
# print("Yangi ro'yhat =", nonushta)
# print('16-MASHQ')
# print(f'Taomlar {taomlar} va nonushta {nonushta}')
# print('17-MASHQ')
# nonushta = ('chuchvara', 'osh', 'xonim', 'manti', 'somsa')
# nonushta[0] = "qaymoq va non"
# nonushta = tuple(nonushta)
# print(nonushta)
'''--------------------9-AMALIYOT------------------------------'''
# print('1-MASHQ')
# ismlar = ['Jamila', 'Kamola', 'Lola', 'Kamila', 'Umida']
# for ism in ismlar:
#   print(f'Yaqin dugonam {ism} sizni tugilgan kunimga taklif qilaman!!!')
# print('2-MASHQ')
# print(f'Kod {len(ismlar)} marta takrorlandi')
# print('3-MASHQ')
# toq_sonlar = list(range(11,100,2))
# for toq in toq_sonlar:
#   print(toq**3)
# print('4-MASHQ')
kinolar = []
print('5ta sevimli kinoyiz: ')
for n in range(5):
  kinolar.append(input(f"{n+1} - sevimli kinoyingiz: "))
print(kinolar)
# print('5-MASHQ')
# soni = int(input('Bugun necha kishi bilan suhbat qildingiz?>>> '))
# odamlar = []
# for n in range(soni):
#   odam = input(f"{n+1} - suhbat qilgan odamingiz kim edi: ")
#   odamlar.append(odam)
# print(odamlar)
'''-----------------10-AMALIYOT----------------------------'''
# print('1-MASHQ')
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car == 'gm':
#     print(car.upper())
#   else:
#     print(car.title())  
# print('2-MASHQ')
# for car in cars:
#   if car != 'gm':
#     print(car.title())
#   else:
#     print(car.upper())  
# print("3-MASHQ")
# login = input('Loginigiz nima?\n')
# if login == 'admin':
#   print(f"Xush kelibsiz,{login.title()}.Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#   print(f"Xush kelibsiz, {login}")
# print('4-MASHQ')
# son1 = input("1-sonni kiriting: ")
# son2 = input('2-sonni kiriting: ')
# if son1 == son2:
#   print('Sonlar teng')
# print('5-MASHQ')
# son = int(input("Istalgan son kiriting: "))
# if son<0:
#   print("Manfiy son")
# else:
#   print("Musbat son")  
# print("6-MASHQ")
# son = int(input("Son kiriting >>> "))
# if son>0:
#   print(son**0.5)
# else: 
#   print("Musbat son kiriting!")  
