# 11-dars
# IF-ELIFE-ELSE
# Sana: 09/08/2022
# Muallif: Nozimjon

# =============================================================================
# son = float(input("Istalgan juft sonni kiriting: "))
# 
# if son % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu juft son emas!")
# =============================================================================

# =============================================================================
# yosh = int(input("Yoshingizni kiriting:\n>>> "))
# 
# if yosh < 4 or yosh > 60:
#     print("Sizga kirish bepul.")
# elif yosh < 18:
#     print("Sizga kirish 10000 so'm")
# else:
#     print("Sizga kirish 20000 so'm")
# =============================================================================

# =============================================================================
# print("Ikkita son kiriting: ")
# son1 = float(input("1-son: "))
# son2 = float(input("2-son: "))
# 
# if son1 == son2: 
#     print("Sonlar teng ekan.")
# elif son1 > son2:
#     print(f"1-son 2-sondan {son1 - son2} taga katta ekan.")
# else:
#     print(f"2-son 1-sondan {son2 - son1} taga katta ekan.")
# =============================================================================

# =============================================================================
# mahsulotlar = ["olma", "banan", "non", "yog'", "piyoz", "kartoshka", "sabzi", "gilos"]
# savat = []
# print("Sotib olmoqchi bo'lgan 5 ta mahsulotingiz nomini kiriting: ")
# 
# for mahsulot in range(5):
#     savat.append(input(f"{mahsulot + 1} - mahsulot nomini kiriting: "))
# 
# for n in savat:
#     if n.lower() in mahsulotlar:
#         print(f"{n.capitalize()} do'konimizda bor.")
#     else:
#         print(f"{n.capitalize()} do'konimizda yo'q ekan.")
# =============================================================================
        

# =============================================================================
# mahsulotlar = ["olma", "banan", "non", "yog'", "piyoz", "kartoshka", "sabzi", "gilos"]
# savat = []
# print("Sotib olmoqchi bo'lgan 5 ta mahsulotingiz nomini kiriting: ")
# 
# for mahsulot in range(5):
#     savat.append(input(f"{mahsulot + 1} - mahsulot nomini kiriting: "))
# 
# bor_mahsulotlar = []
# yoq_mahsulotlar = []
# for n in savat:
#     if n.lower() in mahsulotlar:
#         bor_mahsulotlar.append(n.capitalize())
#     else:
#         yoq_mahsulotlar.append(n.capitalize())
#         
# if yoq_mahsulotlar:
#     print(f"Quyidagi mahsulotlar do'konimizda yo'q: {yoq_mahsulotlar}")
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor ekan!")
# =============================================================================

# =============================================================================
# foydalanuvchilar = ["alisher", "qodir", "sobir", "asil", "jahongir"]
# username = input("O'zingiz uchun login tanlang:\n>>> ")
# 
# if username.lower() in foydalanuvchilar:
#    print("Login band! yangi login tanlang!")
# else:
#    print("Xush kelibsiz qadrli foydalanuvchi!")
# =============================================================================

butun_son = int(input("Istalgan butun son kiriting:\n>>> "))
print(f"{butun_son} 2 dan 10 gacha bo'lgan quyidagi sonlarga qoldiqsiz bo'linadi:")
for i in range(2, 11):
    if butun_son % i == 0:
        print(i)