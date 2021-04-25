''' ######################### 09 FOR TAKRORLASH OPERATORI ########################### '''

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#   print(mehmon)

# ovqatlar = ['makaron', 'osh', 'manti', 'chuchvara']
# for ovqat in ovqatlar:
#   print("=======")
#   print(ovqat)
# print('TAMOM!')
 
# sonlar = [1, 2, 3, 4, 5]
# for son in sonlar:
#   print(2*son)
# print('FOR LOOP tugadi!')

### FOR qanday ishlaydi?
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi")

#     # print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorgi oshga taklif qilamiz\nHurmat bilan, Palonchiyevlar oilasi")

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
    
#     print(mehmonlar) # bu qator tsikl tashqarisida bo'lishi kerak edi


'''for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH'''
# sonlar = list(range(1,11)) # list(range(1,11)) = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")


# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati = [] # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz


# print(sonlar)
# print(sonlar_kvadrati)


'''for va input()'''
# dostlar = []
# print('5ta dostingizni ismini kiriting')
# for n in range(5):
#   dost = input(f"{n+1} - dostingizni ismini kiriting: ")
#   dostlar.append(dost)
# print(dostlar)


'''-------------------------AMALIYOT---------------------'''
# print('1-MASHQ:')
# ismlar = ['Lobar', 'Hilola', 'Lola', 'Munisa', 'Malika', 'Indira']      
# for ism in ismlar:
#   print(f"Hurmatli {ism} dugonam, sizni ertangi soat 8da tug`ilgan kunimga taklif qilaman")
#   print('Hurmat bilan Madina.\n')
  

# print('2-MASHQ:')
# print(f'Kod {len(ismlar)} marta takrorlandi') 


# print('3-MASHQ:')
# toq_sonlar = list(range(11,100,2))#[11,13,....99]
# for toq_son in toq_sonlar:
#   print(toq_son**3)


# print('4-Mashq')
# kinolar = []
# print('5ta sevimli kinoyingiz:')
# for n in range(5):
#   kinolar.append(input(f"{n+1} - sevimli kinoyingiz:"))
# print(kinolar)


# print('5-MASHQ')
# odamlar_soni = int(input("Bugun nechta odam bilan suhbatlashdingiz?"))
# odamlar = []
# for n in range(odamlar_soni):
#   odamlar.append(input (f"{n+1} - odamning ismi nima?"))
# print(odamlar_soni)


print('6-mashq')
kitoblar_soni = int(input("Nechta kitob zakaz bermoqchisiz?"))
kitoblar = []
for n in range(kitoblar_soni):
  kitoblar.append(input(f"{n+1} - kitobingizni nomi nima?"))
print("Siz buyurtma bergan kitoblar", kitoblar)



