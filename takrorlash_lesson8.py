print("1-MASHQ")
'''O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring'''
davlatlar = ['AQSH', 'Turkiya', 'Rossiya', 'Tashkent', 'Janubiy Korea']
print("Ro'yhat =", davlatlar)
print("2-MASHQ")
'''Ro'yxatning uzunligini konsolga chiqaring'''
countries = len(davlatlar)
print("Ro'yhat uzunligi =", countries)
print("3-MASHQ")
'''sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring'''
print(sorted(davlatlar))
print("4-MASHQ")
'''sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring'''
print(sorted(davlatlar, reverse=True))
print("5-MASHQ")
'''Asl ro'yxatni qaytadan konsolga chiqaring'''
print(davlatlar)
print("6-MASHQ")
'''reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring'''
davlatlar.reverse()
print(davlatlar)
print("7-MASHQ")
'''sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.'''
davlatlar.sort()
print("Alifbo boyicha:", davlatlar)
davlatlar.sort(reverse=True)
print("Alifboga teskari:", davlatlar)
print("8-MASHQ")
'''120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing'''
juft_sonlar = list(range(120,1200,2))
print("juft sonlar =", juft_sonlar)
print("9-MASHQ")
'''Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring'''
summa = sum(juft_sonlar)
print("Yigindisi =", summa)
print("10-MASHQ")
'''Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring'''
eng_katta = max(juft_sonlar)
eng_kichik = min(juft_sonlar)
print("Max-min =", eng_katta-eng_kichik)
print("11-MASHQ")
'''Ro'yxatdagi elementlar sonini hisoblang'''
print("Elementlar soni:", len(juft_sonlar))
print("12-MASHQ")
'''Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring'''
boshidan = juft_sonlar[0:20]
print("Royhat boshi:", boshidan)
ortasidan = juft_sonlar[270:290]
print("Royhat ortasi:", ortasidan)
oxiridan = juft_sonlar[520:]
print("Royhat oxiri:", oxiridan)
print("13-MASHQ")
'''taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting'''
taomlar = ['Manti', 'Osh', 'Qozon kabob', 'Somsa', 'Tuxum']
print("Taomlar:", taomlar)
print("14-MASHQ")
'''nonushta degan yangi ro'yxatga taomlardan nusxa oling'''
nonushta = taomlar[:]
print("Nonushta:", nonushta)
print("15-MASHQ")
'''Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing'''
nonushta.remove("Manti")
nonushta.remove('Osh')
nonushta.remove('Qozon kabob')
nonushta.remove('Somsa')
nonushta.append('Pishloq')
nonushta.append('Sut')
print("Yangi nonushta:", nonushta)
print("16-MASHQ")
'''Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring'''
print(f"Taomlar {taomlar} va nonushta {nonushta}")
print("17-MASHQ")
'''Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.'''
breakfast = tuple(nonushta)
print("nonushta", breakfast)
breakfast[0] = "qaymoq va non"
print(breakfast)