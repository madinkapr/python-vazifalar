'''LESSON-14: Dictionary/lug'at bilan ishlash'''

# a = [] # list
# b = () # Tuple
# c = {} # dictionary

# '''1-misol'''
# # {key:value}
# lugat = {'book':'kitob', 'apple':'olma', 'ball':'koptok', 'wall':'devor'}

# tarjima = lugat['apple']
# print(tarjima)

# '''2-misol'''
# dad_car = {'model':'nexia', 'color':'metalic grey', 'yili':'2016', 'yurgan km':200000}
# bro_car = {'model':'lacetti', 'color':'white', 'yili':'2019', 'yurgan km':41000}

# print("Adamning moshinasini rangi", dad_car['color'])
# print(f"Adamning moshinasini rangi {dad_car['color']}")
# print("Akamning moshinasini modeli", bro_car['model'])
# print(f"Akamning moshinasini modeli {bro_car['model']}")

# '''3-misol'''
# talaba_0 = {'ism': 'Madinabonu', 'familya':'Primova', 'birth date': 2002, 'weight': 45.5}
# # .... .... ning tugilgan yili, .... ogirligi 
# # ...
# print(talaba_0['ism'], talaba_0['familya'], "ning tugilgan yili", talaba_0['birth date'], "ogirligi", talaba_0['weight'] )
# print(f"{talaba_0['ism']} {talaba_0['familya']}ning tugilgan yili {talaba_0['birth date']}, ogirligi {talaba_0['weight']}")

# talaba_0['yashash joyi'] = 'Toshkent'
# print(talaba_0)
# talaba_0['dasturlash tili'] = 'Python'
# print(talaba_0)

# '''4-misol'''
# talaba_1 = {} # bo'sh lug'at
# talaba_1['ism'] = 'Hilola'
# talaba_1['familya'] = "Narmatova"
# talaba_1['birth date'] = 2002
# talaba_1['weight'] = 50
# talaba_1['yashash joyi'] = 'Toshkent' 
# talaba_1['dasturlash tili'] = None
# talaba_1['sevimli taomlari'] = ['osh', 'lagmon', 'manti']
# print(talaba_1)
# print('-------')
# # QIYMATNI O'ZGARTIRISH
# talaba_1['yashash joyi'] = 'Xorezm'
# print(talaba_1)
# print('-------')
# # KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH
# del talaba_1['sevimli taomlari']
# print(talaba_1)
# print('-------')

# '''5-misol'''
# ## LUG'ATNI QATORLARGA BO'LIB YOZISH
# talaba_2 = {
#           'ism':'Kamola', 
#           'familya':'Saidqosimova', 
#           'birth data': 2003, 
#           'weight': 52, 
#           'yashash joyi': 'Andijon', 
#           'dasturlash tili': None
#           }

# print(talaba_2)


# '''6-misol'''
# ## get() METODI
# talaba_3 = {
#           'ism':'Sardor', 
#           'familya':'Alimboyev', 
#           'birth data': 2000, 
#           'weight': 62, 
#           'yashash joyi': 'Toshkent vil', 
#           'dasturlash tili': None
#           }
# # phone = talaba_3['telefon'] # KeyError: 'telefon'
# # print(phone)
# phone = talaba_3.get('telefon', 'Bunday key mavjuda emas!')
# print(phone)

'''7-misol'''
lugat = {
            'book'  : 'kitob',
            'apple' : 'olma',
            'wall'  : 'devor',
            'table' : 'stol'
}

# tarjima = lugat['car']
tarjima = lugat.get('car', 'Bunaqa soz lugatda yoq.')
print(tarjima)