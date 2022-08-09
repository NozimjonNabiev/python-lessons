# 7-dars
# Lists (Ro'yxatlar)
# Sana: 09/08/2022
# Muallif: Nozimjon

'''
ismlar = ["Saidumar", "Asil", "laziz"]
print(f"Salom {ismlar[0]}. Qalaysiz? Playstation boramizmi ?\n{ismlar[1]}, bugun futbol bor esdan chiqmasin.\n{ismlar[2]} san esa magazinga borishing kerak ")

sonlar = [10, 150, -80, 90, 10.5, 93]
yigindi = sonlar[0] + sonlar[2]
ayirma = sonlar[3] - sonlar[2]
kopaytma = sonlar[1] * sonlar[-1]
bolinma = sonlar[3] / sonlar[4]
sonlar[4] = 10
sonlar[1] = 149
del sonlar[1]
sonlar.remove(-80)
print(len(sonlar))
print(yigindi)
print(ayirma)
print(sonlar)


t_shaxslar = ["Amir Temur", "Imom al Buxoriy", "Al Beruniy", "Al Xorazmiy"]
z_shaxslar =["Donald Trump", "Mirziyoyev", "Elon Musk", "Bill Gates"]

name1 = t_shaxslar.pop(1)
name2 = z_shaxslar.pop(2)

print(f"Men tarixiy shaxslardan {name1} bilan, zamonaviy shaxslardan esa {name2} bilan suhbat qurishni istar edim")
'''

friends = []
friends.append("Asil")
friends.append("Jahon")
friends.append("Mirjahon")
friends.insert(0, "Sardor")
friends.insert(-1, "Laziz")
friends.insert(2, "Qudrat")
friends.append("Tolib")
# print(friends)

friends.remove("Qudrat")
friends.remove("Mirjahon")
del friends[0]

# print(friends)

friends.insert(0, "Will")
friends.insert(2, "Qalandar")
friends.insert(-1, "Said")

# print(friends)
# print(len(friends))

mehmonlar = []
mehmon1 = friends.pop(0)
mehmon2 = friends.pop(1)
mehmon3 = friends.pop(-1)
mehmon4 = friends.pop(3)
mehmonlar.append(mehmon1)
mehmonlar.append(mehmon2)
mehmonlar.append(mehmon3)
mehmonlar.append(mehmon4)
print(f"Mehmonga keladigan do'stlarim ro'yxati: {mehmonlar}")

