# print('ex-1')
# otam = {'ismi':'Ismoil', 'tugilgan yili': 1958, 'manzili':'Samarqand viloyati'}
# oyim = {'ismi':'Mavluda', 'tugilgan yili': 1966, 'manzili':'Samarqand viloyati'}
# akam_1 = {'ismi':'Eldor', 'tugilgan yili': 1986, 'manzili':'Samarqand viloyati'}
# akam_2 = {'ismi':'Elyor', 'tugilgan yili': 1989, 'manzili':'Toshkent shahri'} 
# print(f"Otamning ismi {otam['ismi']}, {otam['tugilgan yili']}  da, {otam['manzili']}da tug'ilgan")
# print(f"Onamning ismi {oyim['ismi']}, {oyim['tugilgan yili']} da, {oyim['manzili']}da tug'ilgan")
# print(f"Katta akamning ismi {akam_1['ismi']}, {akam_1['tugilgan yili']} da, {akam_1['manzili']}da tug'ilgan")
# print(f"Kichik akamning ismi {akam_2['ismi']}, {akam_2['tugilgan yili']} da, {akam_2['manzili']}da tug'ilgan")

# print('Ex-2')
# sevimli_taom = {'Ibrohim':'osh', 'Madina':'xonim', 'Elyor':'pirog', 'Muhammadyusuf':'norin', 'Eldor':'dimlama'}
# odamlar = ['Eldor', 'Elyor', 'Madina', 'Ibrohim', 'Muhammadyusuf']
# for odam in odamlar:
#     taom = sevimli_taom[odam]
#     print(f"{odam}ning sevimli taomi {taom}")

# print('ex-3')
# izohli_lugat = {'if':'agar',
#                 'else':'aks holda',
#                 'for':'uchun',
#                 'in':'ichida',
#                 'len':'uzunlik',
#                 'list':'royhat',
#                 'integer':'butun son',
#                 'float':'onli son',
#                 'string':'matn'
#                }


# for lugat in izohli_lugat:
#     tarjima = izohli_lugat[lugat] 
#     print(tarjima)
# print('ex-4')    
# soz = input('Kalit soz kiriting:').lower()
# print(izohli_lugat.get(soz, "Bunday soz yo`q"))
# print("Ex-5")
# soz = input('Kalit soz kiriting:').lower()
# if soz==None:
#     print("Bunday soz mavjud emas")
# else:
#     tarjima = izohli_lugat.get(soz, "Bunday soz yo`q")
#     print(f"{soz} sozi {tarjima} deb tarjima qilinadi")    


# print('Ex-1')
# otam = {'ismi':'Ismoil', 'tugilgan yili':1958, 'manzili':'Samarqand viloyati'}
# onam = {'ismi':'Mavluda', 'tugilgan yili':1966, 'manzili':'Samarqand viloyati'}
# akam_1 = {'ismi':'Eldor', 'tugilgan yili':1986, 'manzili':'Samarqand viloyati'}
# akam_2 = {'ismi':'Elyor', 'tugilgan yili':1989, 'manzili':'Toshkent shahri'}
# print(f"Otamning ismi {otam['ismi']}, {otam['tugilgan yili']}da, {otam['manzili']}da tug'ilgan")
# print(f"Onamning ismi {onam['ismi']}, {onam['tugilgan yili']}da, {onam['manzili']}da tug'ilgan")
# print(f"Katta akamning ismi {akam_1['ismi']}, {akam_1['tugilgan yili']}da, {akam_1['manzili']}da tug'ilgan")
# print(f"Kichik akamning ismi {akam_2['ismi']}, {akam_2['tugilgan yili']}da, {akam_2['manzili']}da tug'ilgan")

# print('Ex-2')
# sevimli_taom = {'Adam':'osh', 'Oyim':'mastava', 'Elyor akam':'pirog', 'Eldor akam': 'kotlet', 'Madina':'tabaka'}
# odamlar = ['Adam', 'Oyim', 'Eldor akam', 'Elyor akam', 'Madina']
# for odam in odamlar:
#     taom = sevimli_taom[odam]
#     print(f"{odam}ning sevimli taomi {taom}")
# print('1-Mashq')
# davlat_poytaxtlari = {
#         'Ozbekiston':'Toshkent', 
#         'USA':'Washington', 
#         'Qozogiston':'Ostona'
#         }
# davlat = input("Istalgan davlat kirgizing: ").title()     
# natija = davlat_poytaxtlari.get(davlat, 'Bu davlat bazada yo\'q')
# print(f'{davlat}ning poytaxti {natija}')

# print('2-Mashq')
# keys = ['ten', 'twenty', 'thirty', 'forty', 'fifty']
# vals = [10,20,30,40,50]
# natija = {}
# n = len(keys)
# for i in range(n):
#     x = keys[i]
#     y = vals[i]
#     natija[x] = y
# print(natija)    
# print('3-Mashq')
# students = ['hilola','kamola','madina','ruxsora', 'anvar', 'sardor']
# math_class = [100, 95, 99, 78, 100, 90]
# royhat = {}
# n = len(students)
# for i in range(n):
#     x = students[i]
#     y = math_class[i]
#     royhat[x] = y
# print(royhat)
# print('4-mashq')
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"  
# }

# keysToRemove = ["name", "salary"]
# for key in keysToRemove:
#     del sampleDict[key]
# print(sampleDict)
# print('4-Mashq')
# univerlar = {
#   'TATU': 180,
#   'JIDU': 200,
#   'TMI':  130,
#   'INHA': 140,
#   'TIU':  150
# }
# for k, v in univerlar.items():
#     print(k, v)
# print('5-Mashq')
# ismlar = ['Dad', 'Mom', 'Unkle', 'Aunt', 'nephew', 'niece']
# taomlar = ['Qazon kabob', 'Lagmon', 'Manti', 'Somsa', 'Polov', 'Teftel']
# taom_turi = ['Gosht', 'Xamir', 'Xamir', 'Xamir', 'Guruch', 'Guruch']
# n = len(ismlar)
# res = {}
# for i in range(n):
#   x = ismlar[i]
#   y = taomlar[i]
#   z = taom_turi[i]
#   if z == 'Xamir':
#     res[x] = y
# print(res)    


# davlat_poytaxtlari = {
#         'Ozbekiston':'Toshkent', 
#         'USA':'Washington', 
#         'Qozogiston':'Ostona'
#         }
# davlat = input('Istalgan davlatni kirgizing: ').title()
# natija = davlat_poytaxtlari.get(davlat, 'Bu davlatning poytaxti bazada yo\'q') 
# print(f'{davlat}ning poytaxti {natija}')       
   
# keys = ['ten', 'twenty', 'thirty', 'forty', 'fifty']
# vals = [10,20,30,40,50]
# res = {}
# n = len(keys)
# for i in range(n):
#   x = keys[i]
#   y = vals [i]
#   res[x] = y
# print(res)  


# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"  
# }
# keysToRemove = ["name", "salary"]
# for keys in keysToRemove:
#   del sampleDict[keys]
# print(sampleDict)

# univerlar = {
#   'TATU': 180,
#   'JIDU': 200,
#   'TMI':  130,
#   'INHA': 140,
#   'TIU':  150
# }
# inst = []
# ball = []
# for k, v in univerlar.items():
#   inst.append(k)
#   ball.append(v)
# print(inst)
# print(ball)  

# ismlar = ['Dad', 'Mom', 'Unkle', 'Aunt', 'nephew', 'niece']
# taomlar = ['Qazon kabob', 'Lagmon', 'Manti', 'Somsa', 'Polov', 'Teftel']
# res = {}
# n = len(ismlar)
# for i in range(n):
#   x = ismlar[i]
#   y = taomlar[i]
#   res[x] = y
# print(res)  
   
# taomlar = ['Qazon kabob', 'Lagmon', 'Manti', 'Somsa', 'Polov', 'Teftel']
# taom_turi = ['Gosht', 'Xamir', 'Xamir', 'Xamir', 'Guruch', 'Gosht']
# res = {}
# n = len(taomlar)
# for i in range(n):
#   x = taomlar[i]
#   y = taom_turi[i]
#   res[x] = y
# print(res)  

# taomlar = ['Qazon kabob', 'Lagmon', 'Manti', 'Somsa', 'Polov', 'Teftel']
# taom_turi = ['Gosht', 'Xamir', 'Xamir', 'Xamir', 'Guruch', 'Gosht']
# ismlar = ['Dad', 'Mom', 'Unkle', 'Aunt', 'nephew', 'niece']
# res = {}
# n = len(taomlar)
# for i in range(n):
#   x = taomlar[i]
#   y = taom_turi[i]
#   z = ismlar[i]
#   if y == 'Xamir':
#     res[z] = x
# print(res)

'''---------------------------Oxirgi masala-------------------------'''
print('Ex-1')
# davlat_poytaxtlari = {
#         'Ozbekiston':'Toshkent', 
#         'USA':'Washington', 
#         'Qozogiston':'Ostona'
#         }
# davlat = input('Istalgan davlatizni kiriting: ').title()
# natija = davlat_poytaxtlari.get(davlat, 'Bu davlat bazada yo\'q')
# print(f'{davlat}ning poytaxti {natija}')
print('Ex-2')
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"  
# }
# keysToRemove = ["name", "salary"]
# for keys in keysToRemove:
#   del sampleDict[keys]
# print(sampleDict)  
print('Ex-3')
# univerlar = {
#   'TATU': 180,
#   'JIDU': 200,
#   'TMI':  130,
#   'INHA': 140,
#   'TIU':  150
# }
# inst = []
# ball = []
# for k, v in univerlar.items():
#   inst.append(k)
#   ball.append(v)
# print(inst)
# print(ball)  
print('Ex-4')
taomlar = ['Qazon kabob', 'Lagmon', 'Manti', 'Somsa', 'Polov', 'Teftel']
taom_turi = ['Gosht', 'Xamir', 'Xamir', 'Xamir', 'Guruch', 'Gosht']
ismlar = ['Dad', 'Mom', 'Unkle', 'Aunt', 'nephew', 'niece']
res = {}
n = len(taomlar)
for i in range(n):
  x = taomlar[i]
  y = taom_turi[i]
  z = ismlar[i]
  if y == 'Xamir':
    res[z] = x
print(res)
