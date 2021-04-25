'''------------------------ LESSON-12 ---------------------'''
'''########################XATOLAR BILAN ISHLASH########################'''

## SYNTAXERROR - Sintaksis xato ##

# print("Hello World")
''''
print "Hello World" -->

File "main.py", line 6
    print "Hello World"
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World")?
'''


## EOL va EOF xatolik: EOL - End Of Line; EOF - End Of File
# EOL ga misol: print("Hello World!
# EOF ga misol: print("Hello World!"


## IndentationError - JOY TASHLASHDA XATOLIK
print("Salom!")
'''
print("Salom") # CORRECT
 print("Hello") # IndentationError: unexpected indent'''
'''
for i in range(5):
  if i % 2 == 0:
  print(i, "miz juft son")
print("Helloooo")
'''
# son = 50
# if son>=0:
#     print("Musbat son")
# else:
# print("Manfiy son")


# Run Time Error ga misol
# son = input("Istalgan son kiriting: ")
# print(f"{son} ning kvadrati {son**2} ga teng")


## NameError
# prit("Bonjour") -? print("Bonjour")

# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mvealar:
#     print(meva)

## VALUE ERROR
# son = int(input("Istalgan son kiriting: ")) # int("12")->12  float("12.3")
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")


## INDEX ERROR
# mevalar = ['olma','anor','uzum']
# print(mevalar[3])

## ZeroDivisionError
# x, y = 50, 50
# z = 250/(x-y) # 250/0

## MANTIQIY XATOLAR
# radius = 5
# pi = 4.14 # 3.14
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)

# son = float(input("Istalgan son kiriting: "))
# ildiz = son**1/2# son**1/2 --> son**1 keyin 2ga bolamiz degani. son**(1/2) yoki son**0.5
# print(f"{son} ning ildizi {ildiz} ga teng")

# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi")

# x = 9
# son = int(input('1 dan 10 gacham bolgan men oylagan sonni toping: '))
# if x == son:
#   print("Qarsak!!! Topdingiz!")
# else:
#   print(f'Topolmadingiz, men oylagan son {x} edi')

# '''
# MASALA-1:
# PC: 3ta urinishda men oylagan sonni toping.
# 1-urinish: 1 dan 10 gacham bolgan ixtiyorit son kiriting: X
# "TOPOLMADIZ"/"TOPOLMADIZ"
# 2-urinish: 1 dan 10 gacham bolgan ixtiyorit son kiriting: Y
# "TOPOLMADIZ"/"TOPDINGIZ"
# 3-urinish: 1 dan 10 gacham bolgan ixtiyorit son kiriting: Y
# "TOPOLMADIZ"/"TOPDINGIZ"
# '''
# x = 8
# print("3ta urinishda men oylagan sonni toping.")
# for n in range(3):
#   son = int(input(f'{n+1} - urinish: 1 dan 10 gacham bolgan ixtiyoriy son kiriting: '))
#   if x == son:
#       print("Qarsak!!! Topdingiz!")
#       break
#   else:
#       print('Topolmadingiz')
# print(f"Men o'ylagan son {x} edi.")    

'''
men yaxshi korgan meva bu - Apelsin
PC: "Men yaxshi korgan mevani 5ta urinishda toping!"
1-urinish: "Ixtiyoriy mevani kiriting >>"
"TOPDINGIZ"/Topolmadingiz
...
...
5-urinish: "Ixtiyoriy mevani kiriting >>"
"TOPDINGIZ"/Topolmadingiz

Men oylagan meva Apelsin edi.
'''

my_fruit = "Apelsin"
print("Men yaxshi korgan mevani 5ta urinishda toping!")
for n in range(5):
  meva = (input(f"{n+1} - urinish: Ixtiyoriy mevani kiriting >> ")).title()
  if meva == my_fruit:
    print("TOPDINGIZ")
    break
  else:
    print("TOPOLMADINGIZ")
print(f"Men oylagan meva {my_fruit} edi.")      



