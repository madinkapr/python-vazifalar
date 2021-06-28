# print("1-MASHQ")
# '''Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur'''
# son = int(input("Istalgan sonni toping:>>>\n "))
# kvadrati = son**2
# kubi = son**3
# print(f"{son} ning kvadrati {kvadrati} ga teng")
# print(f"{son} ning kubi {kubi} ga teng")

# print("2-MASHQ")
# '''Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur'''
# yosh = input("Yoshingiz nechida? >>>\n")
# if not yosh.isdigit():
#     print("Iltimos,yoshingizni son bilan kiriting harflar bilan emas!")
# else:
#     yosh = int(yosh)
#     tugilgan_yil = 2021 - yosh
#     if yosh<0 or yosh>120:
#       print("Yoshingizni tori kiriting!")     
#     else:    
#       print(f"Siz {tugilgan_yil} da tug'ilgansiz")

print("3-MASHQ")
'''Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur'''
son_1 = float(input("1-sonni kiriting: "))
son_2 = float(input("2-sonni kiriting: "))
yigindisi = son_1 + son_2
ayirmasi = son_1 - son_2
kopaytmasi = son_1 * son_2
if son_2 == 0:
    bolinmasi = "cheeksizlik"
else:
    bolinmasi = son_1 / son_2       
print(f"Yig'indisi {yigindisi}\nAyirmasi {ayirmasi}\nKopaytmasi {kopaytmasi}\nBolinmasi {bolinmasi}")


        

