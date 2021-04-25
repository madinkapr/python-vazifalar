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

########## SORTED() metodi/funksiyasi ############
# sonlar = [3,2,5,3,1,4,2,7,3]
# # print("Before sonlar: ", sonlar)
# new_sonlar = sorted(sonlar, reverse=True)
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
# mevalar_soni = len(mevalar)
# print(mevalar_soni, "xil mevalar berilgan")

# cars = ["spark", "malibu", "lacetti", "nexia", "damas", "cobalt", "matiz", "tico", "captiva"]
# cars_soni = len(cars)
# print("O`zbekistonda", cars_soni, "xil mashina ishlab chiqariladi")


########## RANGE Funksiysi #############
# print(list(range(0,3)))   # [a,b) -->[0,3]
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
# print(f"Ikki xonali juft sonlar 
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
