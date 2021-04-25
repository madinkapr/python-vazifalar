'''-----------------------Qaytirish [1~12] lessonlar--------------------------''' 
#  print('MASHQ-12: [1,2,44,3,5,32,112, 312,462] sonlarning orta arifmetigi va geometrigini toping!')
# sonlar = [1,2,44,3,5,32,112, 312,462]
# orta_arifmetik = sum(sonlar)/len(sonlar)
# print('Orta arifmetik =', orta_arifmetik)
# kopaytma = 1
# yigindi = 0
# for son in sonlar:
#   kopaytma = kopaytma*son  # 1*2*44*3*5*32...
#   yigindi = yigindi + son  # 1+2+44+3+5+32...
# orta_arifmetik = yigindi/len(sonlar)
# orta_geometrik = kopaytma ** (0.5)
# print('orta arifmetik = ', orta_arifmetik)
# print('orta geometrik =', orta_geometrik)

# import math
# x = math.prod(sonlar)
# orta_geometrik = x**(0.5)
# print('orta geometrik =', orta_geometrik)

# print('---------------------------------------')
# t('MprinASHQ-13: [1002, 100, 539, 299, 2341, 2021, 12, 9, 69, 99] listdan 2-xonali, 3-xonali, 4-xonali sonlarni alohida console ga chiqaring. example:\n2-xonali:[...]\n3-xonali::[...]\n4-xonali:[...]\n')
# sonlar = [1002, 100, 539, 299, 2341, 2021, 12, 9, 69, 99]
# two = []
# three = []
# four = []
# for son in sonlar:
#   if 10<=son<=99:
#     two.append(son)
#   elif 100<=son<=999:
#     three.append(son)
#   elif 1000<=son<=9999:
#     four.append(son)
# print('2-xonali sonlar:', two) 
# print('3-xonali sonlar:', three)    
# print('4-xonali sonlar:', four)

# print('---------------------------------------')
# print('MASHQ-14: [1,2,44,3,5,32,112, 315,462] listdan juft sonlarni avval song toq sonlarni console ga chiqaring!\n')
# sonlar = [1,2,44,3,5,32,112, 315,462]
# juft_sonlar = []
# toq_sonlar = []
# for son in sonlar:
#   if son%2==0:
#     juft_sonlar.append(son)
#   elif son%2 != 0:
#     toq_sonlar.append(son)
# print("Juft sonlar:", juft_sonlar)    
# print("Toq sonlar:", toq_sonlar)



# print('---------------------------------------')
# print("MASHQ-15: [1,2,44,3,5,32,112, 315,462] listdan juft sonlarni yig'indisini toping\n")
# sonlar = [1,2,44,3,5,32,112, 315,462] 
# ## 1-usul
# juft_sonlar = []
# for son in sonlar:
#   if son%2==0:
#     juft_sonlar.append(son)
# print("Juft sonlarni yigindisi =", sum(juft_sonlar))  

# ## 2-usul
# summa = 0
# for son in sonlar:
#   if son % 2 == 0:
#     summa = summa + son

# print("Juft sonlarni yigindisi =", summa)


# print('---------------------------------------')
# print("MASHQ-16: [1,2,44,3,5,32,112, 315,462] listdan toq sonlarni yig'indisini toping\n")
# sonlar = [1,2,44,3,5,32,112, 315,462]
# ## 1-usul
# toq_sonlar = []
# for son in sonlar:
#   if son%2!=0:
#     toq_sonlar.append(son)
# print("Toq sonlar yigindisi =", sum(toq_sonlar))    
# ## 2-usul
# summa = 0
# for son in sonlar:
#   if son%2!=0:
#     summa = summa + son
# print("Toq sonlar yigindisi =", summa) 

# print('---------------------------------------')
# print("MASHQ-17: [1,2,44,3,5,32,112, 315,462] listdan toq sonlarni ko'paytmasini toping. Ex: nums=[1,2,3,4] bo'lsa, kopaytma = 1*3=3\n")
# sonlar = [1,2,44,3,5,32,112, 315,462]
# product = 1
# for son in sonlar:
#   if son%2!=0:
#     product = product * son
# print(f"Toq sonlar kopaytmasi = {product}")    


    

# print('---------------------------------------')
# print("MASHQ-18: [1,2,44,3,5,32,112, 315,462] listdan toq sonlarni o'sish tartibida joylashtiring, so'ng kamayish tartibidas joylashtiring va oxirida original listni console ga chiqaring! \nEx:osish:[1,2,3,5,32,44,112,315,462]\nkamayish:[462,315,112,44,32,5,3,2,1]\norig:[1,2,44,3,5,32,112, 315,462]\n")
# sonlar = [1,2,44,3,5,32,112, 315,462]
# print('Osish:', sorted(sonlar))
# print('Kamayish:', sorted(sonlar,reverse=True)) 
# print('orginal:', sonlar)

# print('---------------------------------------')
# print ("MASHQ-19: ['osh', 'lagmon', 'manti', 'somsa', 'chuchvara', 'mastava', 'shashlik'] listni alfabit o'sish tartibida joylashtiring\n")
# ovqatlar = ['osh', 'lagmon', 'manti', 'somsa', 'chuchvara', 'mastava', 'shashlik']
# print(sorted(ovqatlar))


# print('---------------------------------------')
# print("MASHQ-20: userdan ismini sorang. Song userdan yoshini sorang.\nAgar user yoshi 10 dan kichik bolsa, USER_NAME, sizga bilet tekin.\nAgar user yoshi 60 dan katta bolsa, USER_NAME aka/opa, sizga bilet tekin.\n Aks holda USER_NAME, sizga bilet 1000 somdan sotiladi. deb console ga chiqaring.\n")
# ism = input("Ismngiz nima?").title()
# yosh = int(input('Yoshingiz nechida?'))
# if yosh<10:
#   print(f'{ism}, sizga bilet tekin')
# elif yosh>60:
#   print(f"{ism} aka/opa, sizga bilet tekin") 
# else:
#   print(f'{ism}, sizga bilet 1000 somdan sotiladi')   

# print('---------------------------------------')
# print("MASHQ-20: [0,23,14,11,12,54,55,56,60,67] listdagi sonlarning juftlarini")
# sonlar = [0,23,14,11,12,54,55,56,60,67]
# for son in sonlar:
#   if son%2==0:
#     print(son)

# print('---------------------------------------')
# print("MASHQ-21: [10,23,14,11,12,54,55,56,60,67] listdagi sonlarning juftlarining index lari va qiymatlarini consolega chiqaring:\nEx:\nindex:value\n0:10\n2:14\n4:14\n...\n")
# sonlar = [10,23,14,11,12,54,55,56,60,67] # [0,2,4,5,7,8]
# result = []
# for index in range(len(sonlar)):
#   if sonlar[index]%2==0:
#     # print(index, ':', sonlar[index])
#     result.append( (index, sonlar[index]) )
# print(result)
