######## Lesson-5: STRING (MATN) #############

# ### F-STRING ####
# s = f"Mening ismim {fio}"
# print(s)

# upper() va lower()
# first_name = "Eldor"
# second_name = "Primov"
# fathers_name = "Ismoilovich"
# fio = first_name + " " + second_name + " " + fathers_name
# print(fio)
# # TODO: use f-string
# fio = f"{first_name} {second_name} {fathers_name}"
# print(fio)

# FIO = fio.upper()
# print(FIO)

# fio = FIO.lower()
# print(fio)

# matn = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# kichkina_matn = matn.lower()
# print(kichkina_matn)
# print(matn.lower())
# print(matn)
# poytaxt = "toshkent" 
# print(poytaxt.upper())
# print(poytaxt)
# poytaxt = poytaxt.upper()

# poytaxt = "samarqand"
# print(f"poytaxt = {poytaxt}")
# poytaxt = poytaxt.upper() #"TOSHKENT"
# print(f"poytaxt = {poytaxt}")

# # title() va capitalize()
# name = 'eldor primov ismoilovich' # "eldor"
# print(name.title())
# family_name = "eldor primov ismoilovich" # "primov"
# print(family_name.capitalize())

# #### strip(), rstrip() va lstrip() 
#matn = "  SHIRIN    OLMA      "
#print(matn)
#print(matn.strip() + "!")
#print(matn.lstrip() + "!")
#print(matn.rstrip() + "!")

#"""INPUT — FOYDALANUVCHI BILAN MULOQOT"""
#ism = input("Ismingiz nima?\n")
#print(f"Salom, {ism.title()}!")

#fio = input("To`liq ismingizni kiriting\n")
#print(f"Tanishganimdan xursandman, {fio.title()}!")



""" ------------ UY ISHI ---------- """
# #1) Quyidagi o'zgaruvchilarni yarating: 
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(kocha)
# print(mahalla)
# print(tuman)
# print(viloyat)

# #2) Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# kocha = 'Bog\'bon kochasi'
# mahalla = 'Sog\'bon mahallasi'
# tuman = 'Bodomzor tumani'
# viloyat = 'Samarqand viloyati'
# print(kocha + ", " + mahalla + ", " + tuman + ", " + viloyat)
# print(f'{kocha}, {mahalla}, {tuman}, {viloyat}')

#3) Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# kocha = input("Ko`changizning nomi nima?\n")
# mahalla = input("Mahallangiz nomi nima?\n")
# tuman = input("Tumaningiz nima?\n")
# viloyat = input("Viloyatingiz nima?\n")
# print(kocha + ", " + mahalla + ", " + tuman + ", " + viloyat)
# print(f'{kocha}, {mahalla}, {tuman}, {viloyat}')


# #4) Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# print(kocha + ", \n" + mahalla + ", \n" + tuman +", \n" + viloyat + "\n" )
# print(f'{kocha},\n{mahalla},\n{tuman},\n{viloyat}')

# #5) Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
# yangi_manzil = f"{kocha}, {mahalla}, {tuman}, {viloyat}"

# #6) manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring
# print(f"ORIGNAL:\n{yangi_manzil}")
# print("UPPER() ning ishlatilishi:")
# print(yangi_manzil.upper())
# print("LOWER() ning ishlatilishi:")
# print(yangi_manzil.lower())
# print("TITLE() ning ishlatilishi:")
# print(yangi_manzil.title())
# print("CAPITILIZE() ning ishlatilishi:")
# print(yangi_manzil.capitalize())

# #7-8) Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# # * Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

#9)Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang

# kocha = input("kochangizni nomi nima?")
# mahalla = input("mahallangiz nomi nima?")
# tuman = input("tumaningiz nomi nima?")
# viloyat = input("viloyatingiz nomi nima?")
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

