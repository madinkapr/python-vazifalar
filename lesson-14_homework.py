print('ex-1')
otam = {'ismi':'Ismoil', 'tugilgan yili': 1958, 'manzili':'Samarqand viloyati'}
oyim = {'ismi':'Mavluda', 'tugilgan yili': 1966, 'manzili':'Samarqand viloyati'}
akam_1 = {'ismi':'Eldor', 'tugilgan yili': 1986, 'manzili':'Samarqand viloyati'}
akam_2 = {'ismi':'Elyor', 'tugilgan yili': 1989, 'manzili':'Toshkent shahri'} 
print(f"Otamning ismi {otam['ismi']}, {otam['tugilgan yili']}  da, {otam['manzili']}da tug'ilgan")
print(f"Onamning ismi {oyim['ismi']}, {oyim['tugilgan yili']} da, {oyim['manzili']}da tug'ilgan")
print(f"Katta akamning ismi {akam_1['ismi']}, {akam_1['tugilgan yili']} da, {akam_1['manzili']}da tug'ilgan")
print(f"Kichik akamning ismi {akam_2['ismi']}, {akam_2['tugilgan yili']} da, {akam_2['manzili']}da tug'ilgan")

print('Ex-2')
sevimli_taom = {'Ibrohim':'osh', 'Madina':'xonim', 'Elyor':'pirog', 'Muhammadyusuf':'norin', 'Eldor':'dimlama'}
odamlar = ['Eldor', 'Elyor', 'Madina', 'Ibrohim', 'Muhammadyusuf']
for odam in odamlar:
    taom = sevimli_taom[odam]
    print(f"{odam}ning sevimli taomi {taom}")

print('Ex-3')    
izohli_lugat = {'integer':'butun son', 
                'foat':'onli son', 
                'string':'matn', 
                'if':'agar', 
                'else':'aks holda', 
                'list':'royhat', 
                'sort':'tartiblash', 
                'del':'ochirish', 
                'for':'uchun', 
                'and':'va'
               }
for lugat in izohli_lugat:
    tarjima = izohli_lugat[lugat]
    print(tarjima)

print('Ex-4')
soz = input('Kalit soz kiriting:').lower()
print(izohli_lugat.get(soz,"Bunda so'z mavjud emas"))

print('Ex-5')
soz = input('Kalit soz kiriting:')
if soz==None:
    print("Bunday so'z mavjud emas")
else:    
print(f"{soz} so'zi {tarjima} deb tarjima qilinadi")
