# 25-dars: Son topish o'yini
# Sana: 12/08/2022
# Muallif: Nozimjon Nabiev

import random 

def son_top(value=100):
    print("\nKeling o'ylagan sonni topish o'ynaymiz!")
    taxmin = int(input("\n1 dan 100 gacha son o'yladim. Topa olasizmi?:\n>>> "))
    son = random.randint(1, value)
    counter = 1
    
    while True:
        if taxmin == son:
            print(f"\nTOPDINGIZ! {son} sonini o'ylagan edim. {counter} ta urinishda topdingiz! Tabriklayman!")
            break
        elif son > taxmin:
            taxmin = int(input("Xato, men o'ylagan son bundan kattaroq. Yana urinib ko'ring:\n>>> "))
            counter += 1
        elif son < taxmin:
                taxmin = int(input("Xato, men o'ylagan son bundan kichikroq. Yana urinib ko'ring:\n>>> "))
                counter += 1
    return counter


def son_top_pc(qiymat=100):
    print("\n1 dan 100 gacha son o'ylang. Men topishga harakat qilaman:")
    input("O'ylagan soningizni kiriting:(Kiritib bo'lgach, istalgan tugmani bosing) ")
    komp_taxmin = random.randint(1, qiymat)
    javob = input(f"Siz {komp_taxmin} sonini o'yladingiz: to'g'ri(T), men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)?? ").lower()
    yuqori = qiymat
    quyi = 1
    count = 1
    while True:
        if javob == 't':
            print(f"\nSoningizni {count} ta taxmin bilan topdim!")
            break
        elif javob == '+':
            quyi = komp_taxmin + 1
            komp_taxmin = random.randint(quyi, yuqori)
            javob = input(f"Siz {komp_taxmin} sonini o'yladingiz: to'g'ri(T), men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)?? ").lower()
            count += 1
        elif javob == '-':
              yuqori = komp_taxmin - 1
              komp_taxmin = random.randint(quyi, yuqori)
              javob = input(f"Siz {komp_taxmin} sonini o'yladingiz: to'g'ri(T), men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)?? ").lower()
              count += 1
    return count


def oyna(x=100):
    yana = True
    while yana:
        taxminlar_user = son_top(x)
        taxminlar_pc = son_top_pc(x)
        if taxminlar_pc < taxminlar_user:
            print(f"\nMen {taxminlar_pc} ta taxmin bilan g'olib bo'ldim.")
        elif taxminlar_user < taxminlar_pc:
            print(f"\nTabriklayman! Siz {taxminlar_user} ta taxmin bilan g'olib bo'ldingiz!")
        else:
            print(f"\n{taxminlar_pc}:{taxminlar_user} DURRANG!")
            
        yanami = int(input("Yana o'ynashni xohlaysizmi? ha - 1, yo'q - 0: "))
        if yanami == 1:
            yana = True
        else:
            print("\nO'yin uchun tashakkur! Umid qilamanki sizga yoqdi.")
            break

sontop = oyna()    
        


