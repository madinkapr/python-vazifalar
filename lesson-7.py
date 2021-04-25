'''+++++++++++++++07 LIST (RO'YXAT)+++++++++++++++'''
# uncles_list = ["Yahyo", "Akmal", "Baxtiyor", "Ixtiyor"]
# print("Tog`alar listi =", uncles_list)
# aunts_list = ["Masuda", "Marusa", "Shohida"]
# print("Xolalar listi =", aunts_list)
# months_list = ["January", "February", "March"]
# print(f"Oylar listi = {months_list}")
# family_birthday_list = [1958, 1966, 1986, 1989, 2002]
# print("oilalar listi = " + str(family_birthday_list))
# vazn_list = [69.3, 80, 79.5, 85, 46.2]
# print("Vazn listi =", vazn_list)
# aralash_list = ["Eldor", 1986, 79.5]
# print(f"Aralash list = {aralash_list}")

#######List elementlari va indekslari#######
# baholar = [1, 2, 3, 4, 5]
# #          0, 1, 2, 3, 4
# chetElBoholar = ["A+", "A", "B+", "B", "C+", "C", "F"]
# #                 0.    1.   2.    3.   4.    5.   6
# #                -7.    -6. -5.   -4.  -3.   -2.  -1
# element = chetElBoholar[-8]
# print(element) 

# kitoblar = ["Matem", "ona-tili", "Fizika", "English"]
# narhlar = [12000, 5990, 10000, 15000]
# ## ######Kichik amaliyot: #######
# # Matem: 12000
# # ona-tili: 5990
# # Fizika: 10000
# # English: 15000
# print(kitoblar[0], narhlar[0])
# print(kitoblar[1], narhlar[1])
# print(kitoblar[2], narhlar[2])
# print(kitoblar[3], narhlar[3])
# print('*************************')
# print("Matem", narhlar[0])
# print("Ona-tili", narhlar[1])
# print("Fizika", narhlar[2])
# print("English", narhlar[3])


# kitoblar = ["Matem", "ona-tili", "Fizika", "English"]
# narhlar = [12000, 5990, 10000, 15000]

''' matem va fizika kitoblarini xarid qilishimiz kerak. Necha so'm bo'ladi? '''
# pul = narhlar[0] + narhlar[2]
# print(pul)
'''Masala: Quyidagi ko'rinishda printga chiqarish'''
# # MATEM: 12000
# # ONA-TILI: 5990
# # FIZIKA: 10000
# # English: 15000
# print(kitoblar[0].upper(), narhlar[0])
# print(kitoblar[1].upper(), narhlar[1])
# print(kitoblar[2].upper(), narhlar[2])
# print(kitoblar[3].upper(), narhlar[3])

''' Fizika kitobimizning narxi 1200 so'mga qimmatlashdi, English esa 500 so'mga arzonlashdi'''
# narhlar[2] = 11200
# narhlar[3] = 14500
# print(kitoblar[0].upper(), narhlar[0])
# print(kitoblar[1].upper(), narhlar[1])
# print(kitoblar[2].upper(), narhlar[2])
# print(kitoblar[3].upper(), narhlar[3])

# narhlar[2] = narhlar[2] + 1200
# narhlar[3] = narhlar[3] - 500

# print(kitoblar[0].upper(), narhlar[0])
# print(kitoblar[1].upper(), narhlar[1])
# print(kitoblar[2].upper(), narhlar[2])
# print(kitoblar[3].upper(), narhlar[3])

#### Listga yangi element qo'shish #####
# mevalar = ['olma', 'anor', 'shaftoli', 'ananas', 'mandarin', 'banana', 'gilos']
# yangi_meva = 'apelsin'
# mevalar.append(yangi_meva)
# print(mevalar)
# yangi_meva = 'kivi'
# mevalar.append(yangi_meva)
# print(mevalar)
# yangi_meva = "anjir"
# mevalar.append(yangi_meva)
# print(mevalar)
# mevalar.append('olxori')
# print(mevalar)
# mevalar.append('olxori')
# print(mevalar)

#### INSERT() metodi/funksiyasi ####
# cars = ['tico', 'damas', 'nexia']
# new_car = 'cobalt'
# cars.append(new_car)
# print(cars)
# first_car = 'BMW'
# cars.insert(2, first_car)
# print(cars)

#### Elementlarni o'chirish ####
# cars = ['tico', 'damas', 'nexia', 'malibu', 'cobalt']
# car = 'damas'
# cars.remove(car)
# cars.remove('malibu')
# print(cars)

### Elementni sug'irib olish ###
# vagonlar = ['vagon1', 'vagon2', 'vagon3', 'vagon4']
# print("dastlabki vagonlar ro'yxati:" , vagonlar)
# uzilgan_vagon = vagonlar.pop(0)
# print('uzilgan vagon:', uzilgan_vagon)
# print('vagonlar:', vagonlar)




''' >>>>>>>>>>>>>>>>AMALIYOT<<<<<<<<<<<<< '''
#1.ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar_list = ["Lobar", "Kamola", "Hilola"]
print("Ismlar ro`yhati =", ismlar_list)
#2. Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
print(ismlar_list[0], "eng yaqin dugonam!")
print(f"{ismlar_list[1]} va {ismlar_list[2]} mening kursdoshlarim!")
#3. sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [2, 3, -5, -7, 6.7, 9.2, -6.0] 
print(sonlar)
#4. Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
natija = sonlar[0] + sonlar[1] 
print("sonlar[0] + sonlar[1] =", natija) 
natija = sonlar[5] - sonlar[4]
print("sonlar[5] - sonlar[4] =", natija)
natija = sonlar[1] / sonlar[0]    
print("sonlar[1] : sonlar[0] =", natija) 
sonlar[2] = -15
sonlar[4] = 9.2
sonlar[5] = 6.7
print(sonlar)
#5. t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
t_shaxslar = ["Amir Temur", "Mirzo Ulug`bek", "Alisher Navoiy"]
z_shaxslar = ["Mirziyoyev", "Elon Musk", "Bill Gates"]
print(t_shaxslar)
print(z_shaxslar)
# 6.Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print("Men tarixiy shaxslardan", t_shaxslar.pop(0), "bilan,\nzamonaviy shaxslardan esa", z_shaxslar.pop(0), "bilan\nsuhbat qilishni istar edim")
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim")
# 7.friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends = []
friends.append("Lobar")
friends.append("Hilola")
friends.append("Kamola")
friends.append("Dilbar")
print(friends)
# 8.Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends.remove("Lobar")
print(friends)
friends.remove("Hilola")
print(friends)
# 9.Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0, "Lola")
friends.insert(1, "Zarnigor")
friends.append("Qizlarxon")
print("Friends = ", friends)
# 10.Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
yangi_mehmonlar = []
friend = friends.pop()
yangi_mehmonlar.append(friend)
print("Friends =", friends)
print("Yangi mehmonlar =", yangi_mehmonlar)

friend = friends.pop()
yangi_mehmonlar.append(friend)
print("Friends =", friends)
print("Yangi mehmonlar =", yangi_mehmonlar)

friend = friends.pop()
yangi_mehmonlar.append(friend)
print("Friends =", friends)
print("Yangi mehmonlar =", yangi_mehmonlar)

friend = friends.pop()
yangi_mehmonlar.append(friend)
print("Friends =", friends)
print("Yangi mehmonlar =", yangi_mehmonlar)

friend = friends.pop()
yangi_mehmonlar.append(friend)
print("Friends =", friends)
print("Yangi mehmonlar =", yangi_mehmonlar)

