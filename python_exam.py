'''Task-1 userdan ismini kiritishni sorang.
# Birinchi harfni katta qolganlarini kichkinada consolega chiqaring.'''
# ism = input('Ismingizni kiriting: ').title()
# print(f'Salom, {ism}')
'''Task-2 "Bu inson 'ulug'' kishidir." 
Manashu matnni consolega chiqaring'''
# print('''"Bu inson \'ulug'\' kishidir"''')
'''Task-3 [3,4,2,13,7] 
a)osish tartibida chiqarin
b)kamayish tartibida chiqarin 
c)originalni consolega chiqarin'''
# x = [3,4,2,13,7]
# print(f"Osish tartibda: {sorted(x)}")
# print(f"Kamayish tartibida: {sorted(x, reverse=True)}")
# print("Original:", x)
'''Task-4 nums = [1,2,3] ni yangi new_nums ga kochirin.
Songra numsga '5' ni qoshing.Nums va new_nums ni consolega chiqarin'''
# nums = [1,2,3]
# new_nums = nums[:]
# nums.append(5)
# print("sonlar =", nums)
# print('yangi sonlar =', new_nums)
'''TAsk-5 L1=[1,2,3,4] L2=[5,6,7,8] mos orindagi sonlarni qoshing va 
consolega chiqarin javobi L3 = [6,8,10,12] chiqishi kere'''
L1=[1,2,3,4]
L2=[5,6,7,8]
L3 = []
n = len(L1)
for i in range(n):
    k = L1[i]+L2[i]
    L3.append(k)
print('L3 =', L3)

