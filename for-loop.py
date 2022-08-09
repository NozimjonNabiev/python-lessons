# 9-dars
# FOR LOOP
# Sana: 09/08/2022
# Muallif: Nozimjon

'''
ismlar =["Asil", "Vali", "Sobir", "Qodir", "Jalol"]

for ism in ismlar:
    print("Salom, " + ism)
print(f"Kod {len(ismlar)} marta takrorlandi")

toq_sonlar = list(range(11,100, 2))
for son in toq_sonlar:
    print(son ** 3)
    
kinolar = []
print("5 ta eng sevimli kinolaringizni nomini kiriting:")
for n in range(5):
    kinolar.append(input(f"{n+1} - sevimli kinongizni nomini kiriting: "))
print(f"Sizning sevimli kinolaringiz: {kinolar}")
'''

odamlar_soni = int(input("Bugun nechta odam bilan uchrashdingiz:\n>>> "))
odamlar = []

for odam in range(odamlar_soni):
    odamlar.append(input(f"{odam+1} - uchrashgan odamingiz nomini kiriting: "))
print(f"Siz bugun {odamlar_soni} ta odam(lar) bilan uchrashgansiz. Ularning nomlari {odamlar} ")
    