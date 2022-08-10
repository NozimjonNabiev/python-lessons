# 17-dars: INPUT() VA WHILE
# Sana: 10/08/2022
# Muallif: Nozimjon Nabiev

#                            Task 1
# savol = "Yaxshi ko'rgan kitobingiz nomini kiriting(dasturdan chiqish uchun stop so'zini kiriting):\n>>> " 
    
# savol1 = input(savol)

# while True:
#     savol1 = input(savol)
#     if savol1 == 'stop':
#         break
    

# =============================================================================
#                       Task 2
# =============================================================================
# savol = "Yoshingizni kiriting:(dasturdan chiqish uchun exit yoki quit deb yozing!)\n>>> "

# flag = True 

# while flag:
#     ask = input(savol)
#     if ask == 'exit' or ask == 'quit':
#         break
    
#     yosh = int(ask)
#     if yosh <= 7:
#         print("Sizga kirish 2000 so'm.")
#     elif yosh <= 18:
#         print("Sizga kirish 3000 so'm.")
#     elif yosh <= 65:
#         print("Sizga kirish 10000 so'm.")
#     else:
#         print("Sizga kirish bepul.")
            

# Task 3
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol).lower()
#     if qiymat=='exit':
#        break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")