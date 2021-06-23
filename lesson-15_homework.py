'''
HomeWork-1:
Python izohli lug'atini yarating
va lug'atga kamida 10 ta so'z qo'shing.
Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, 
alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 

Javobi console da quyidagicha chiqishi kerak:

'Boolean' - 'Mantiqiy qiymat',
'Float'   - 'O\'nlik son',
'For'     - 'Biror amalni qayta bajarish tsikli',
'If'      - 'Shartni tekshirish operatori',
'Integer' - 'Butun son'
...
...'''
# Dict = {
#   'Boolean' : 'Mantiqiy qiymat',
#   'Float'   : 'O\'nlik son',
#   'For'     : 'Biror amalni qayta bajarish tsikli',
#   'If'      : 'Shartni tekshirish operatori',
#   'Integer' : 'Butun son',
#   'Len()'   : 'listni uzunligi',
#   'Type()'  : 'turi',
#   'Append'  : 'qo\'shish',
#   'Values'  : 'qiymatlar',
#   'Del'     : 'o\'chirish'
# }
# for k, v in sorted(Dict.items()):
#     print(f"{k} - {v}")
'''
Homework-2
Davlatlar va ularning poytaxtlari lug'atini tuzing. 
Avval lug'atdagi davlatlarni, 
keyin poytaxtlarni alohida-alohida, 
alifbo ketma-ketligida konsolga chiqaring. 

Javobi console da quyidagicha chiqishi kerak:
Dunyo davlatlari:              Davlatlarning poytaxtlari:
AQSH                           Bishkek
ITALIYA                        Dushanbe
MALAYZIYA                      Kuala-Lumpur
O'ZBEKISTON                    Moskva
QIRG'IZISTON                   Nursulton
QOZOG'ISTON                    Rim
ROSSIYA                        Singapur
SINGAPUR                       Toshkent
TOJIKISTON                     Washington D.C.
'''
Mamlakatlar = {
    'AQSH' : 'Washington D.C.',
    'QOZOG\'ISTON' : 'Nursulton',
    'TOJIKISTON' : 'Dushanbe',
    'O\'ZBEKISTON' : 'Toshkent',
    'ITALIYA' : 'Rim',
    'MALAYZIYA' : 'Kuala-Lumpur',
    'ROSSIYA' : 'Moskva',
    'SINGAPUR' : 'Singapur',
    'QIRG\'IZISTON' : 'Bishkek'
}
# davlatlari = []
# poytaxtlari = []
# for k, v in Mamlakatlar.items():
#     davlatlari.append(k)
#     poytaxtlari.append(v)
# davlatlari.sort()   
# poytaxtlari.sort() 
# print('Dunyo davlatlari: \n', davlatlari)
# print('Davlatning poytaxtlari: \n', poytaxtlari)
''' Homework-3
Foydalanuvchidan istalgan davlatni kiritishni so'rang va
 shu davlatning poytaxtini konsolga chiqaring. 
 Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,
  "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

Javobi console da quyidagicha chiqishi kerak:
Qaysi davlatning poytaxtini bilishni istaysiz?: AQSH
AQSHning poytaxti Washington D.C shahri

Qaysi davlatning poytaxtini bilishni istaysiz?:Germaniya
Kechirasiz, bizda bu haqida ma'lumot yo'q
'''
# davlat = (input('Qaysi davlatning poytaxtini bilishni istaysiz?: ')).upper()
# x = Mamlakatlar.get(davlat, "-1")
# print('x =', x)
# if x == "-1":
#   print("Bizda bunday ma\'lumot yo\'q")
# else:
#   print(f"{davlat}ning poytaxti {x} shahri")

'''Homework- 4
Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
agar taom menuda bo'lsa narhini ko'rsating, 
aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
'''
# menyu = { 
#     'osh' : 20000,
#     'lagmon' : 25000,
#     'manti' : 10000,
#     'non' : 4000,
#     'shorva' : 8000,
#     'shashlik' : 15000,
#     'manpar' : 9000,
#     'kabob' : 30000,
#     'somsa' : 5000,
#     'salat' : 6000
# }
# print('3ta taom buyurtma bering.\n')
# for i in range(3):
#     taom = input(f'{i+1}-taom:')
#     x = menyu.get(taom, 'Bizda bunday taom yo\'q')
#     if x == 'Bizda bunday taom yo\'q':
#         print(f'Kechirasiz, bizda {taom} yo\'q')
    


# Dict = {
#   'Boolean' : 'Mantiqiy qiymat',
#   'Float'   : 'O\'nlik son',
#   'For'     : 'Biror amalni qayta bajarish tsikli',
#   'If'      : 'Shartni tekshirish operatori',
#   'Integer' : 'Butun son',
#   'Len()'   : 'listni uzunligi',
#   'Type()'  : 'turi',
#   'Append'  : 'qo\'shish',
#   'Values'  : 'qiymatlar',
#   'Del'     : 'o\'chirish'
# }
# for k,v in sorted(Dict.items()):
#   print(f"{k} - {v}")


Mamlakatlar = {
    'AQSH' : 'Washington D.C.',
    'QOZOG\'ISTON' : 'Nursulton',
    'TOJIKISTON' : 'Dushanbe',
    'O\'ZBEKISTON' : 'Toshkent',
    'ITALIYA' : 'Rim',
    'MALAYZIYA' : 'Kuala-Lumpur',
    'ROSSIYA' : 'Moskva',
    'SINGAPUR' : 'Singapur',
    'QIRG\'IZISTON' : 'Bishkek'
}
# davlatlar = []
# poytaxtlar = []
# for k,v in Mamlakatlar.items():
#   davlatlar.append(k)
#   poytaxtlar.append(v)
# sorted(davlatlar)
# sorted(poytaxtlar) 
# print("Dunyo davlatlari: \n", davlatlar) 
# print("Dunyo poytaxtlari: \n", poytaxtlar)


# davlat = input("Qaysi davlatning poytaxtini bilishni istaysizmi?").title()
# country = Mamlakatlar.get(davlat, "Bizda bunday ma'lumot yo'q")
# print(f"{davlat}ning poytaxti {country} shahri")

menyu = { 
    'osh' : 20000,
    'lagmon' : 25000,
    'manti' : 10000,
    'non' : 4000,
    'shorva' : 8000,
    'shashlik' : 15000,
    'manpar' : 9000,
    'kabob' : 30000,
    'somsa' : 5000,
    'salat' : 6000
}
ovqat = input("3ta taom buyurtma bering. \n")
for i in range(3):
    taom = input(f"{i+1} - taom: ")



