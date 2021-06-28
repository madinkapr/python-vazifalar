# print("1-MASHQ")
# '''ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting'''
# ismlar = ['Kamola', 'Hilola', 'Xadicha']
# print(ismlar)
# print('2-MASHQ')
# '''Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: '''
# print(f"Salom {ismlar[0].title()}, qalesan?")
# print(f"Men, {ismlar[1].title()}, va {ismlar[2].title()} birga aylanishga bordik.")
# print('3-MASHQ')
# '''sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).'''
# sonlar = [2, 3, 4, -5, 2.2, -4, 6.2, -1.5, 8.5]
# print(sonlar)
# print('4-MASHQ')
# '''Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. '''
# yigindi = sonlar[0] + sonlar[2]
# ayirma = sonlar[3] - sonlar[5]
# kopaytma = sonlar[0] * sonlar[1]
# bolinma = sonlar[3] / sonlar[5]
# print('sonlar[0] + sonlar[2] =', yigindi)
# print('sonlar[3] - sonlar[5] =', ayirma)
# print('sonlar[0] * sonlar[1] =', kopaytma)
# print('sonlar[3] / sonlar[5] =', bolinma)
# sonlar[0] = 1
# sonlar[1] = 2
# sonlar[2] = 3
# print(sonlar)
# print('5-MASHQ')
# '''t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating
# va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning,
# ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.'''
# t_shaxslar = ['Islom Karimov', 'Amir Temur', 'Mirzo Ulug\'bek']
# z_shaxslar = ['Shavkat Mirziyoyev', 'Jeki Chan', 'Shoxruhxon'] 
# print("Tarixiy shaxslar:", t_shaxslar)
# print("Zamonaviy shaxslar:", z_shaxslar)
# print('6-MASHQ')
# '''Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:'''
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\nzamonaviy shaxslardan {z_shaxslar.pop(2)} bilan\nsuhbatlashni istardim")
print('7-MASHQ')
'''friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. '''
friends = []
friends.append('Lobar')
friends.append('Shahlo')
friends.append('Fotima')
friends.append('Xadicha')
friends.append('Nigina')
friends.append('Kamola')
friends.append('Hilola')
print(friends)
print('8-MASHQ')
'''Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.'''
friends.remove('Kamola')
friends.remove('Hilola')
friends.remove('Lobar')
print(friends)
print('9-MASHQ')
'''Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.'''
friends.append('Yulduz')
friends.insert(0, 'Malika')
friends.insert(3, 'Jasmina')
print(friends)
print('10-MASHQ')
'''Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. 
 .pop() va .append() metodlari yordamida 
 mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, 
 mehmonlar ro'yxatiga qo'shing.'''
new_friends = []
new_friends.append(friends.pop(0))
new_friends.append(friends.pop(2))
new_friends.append(friends.pop())
print("Yangi mehmonlar:", new_friends)
print("Friends:", friends)


