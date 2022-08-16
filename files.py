# 33-dars: FAYLLAR BILAN ISHLASH
# Sana: 16/08/2022
# Muallif: Nozimjon Nabiev

# import pickle
# with open('fayllar.txt', 'r') as file:
#     info = file.read()

# print(info)

# with open('pi_million_digits.txt', 'r') as fayl:
#     pi = fayl.read()

# birthday = int(input("Tug'ilgan kuningizni kiriting:(Masalan:12-mart 2002-yilni 12032002): "))
# birthday2 = str(birthday)
# if birthday2 in pi:
#     print("PI sonida sizning tug'ilgan kuningiz mavjud ekan))")
# else:
#     print("Afsuski topolmadim((")


# with open('pi_million_digits.txt', 'r') as fayl:
#      pi = fayl.read()
     
# pi = pi.rstrip()
# pi.replace('\n','')
# pi.replace(' ', '')
# # pi = float(pi)
# # print(pi)

# with open('info', 'wb') as file:
#     pickle.dump(pi, file)

# with open('info', 'rb') as newfile:
#     pi2 = pickle.load(newfile)

# print(pi2)

# savollar = ['Ismingiz nima? ', "Yoshingiz nechada? ", "Yaxshi ko'rgan filmingizni nomi nima? " ]
# javoblar = ['Ismi: ', 'Yoshi: ', 'Sevimli kinosi: ']

# for i in range(3):
#     ask = input(savollar[i])
#     with open('savol-javob', 'a') as file:
#         file.write(javoblar[i] + ask + '\n')

# with open('savol-javob', 'r') as test:
#     checking =  test.read()

# print(checking)