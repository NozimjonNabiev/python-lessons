# 8-dars
# Ro'yxatlar bilan ishlash
# Sana: 09/08/2022
# Muallif: Nozimjon

'''
davlatlar = ["Russia", "USA", "France", "Great Britain", "China", "India", "Uzbekistan"]
print(len(davlatlar))
print(sorted(davlatlar))
#print(sorted(davlatlar, reverse=True))
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
'''
'''

juft_sonlar = list(range(120, 1200, 2))
# print(juft_sonlar)
print(f"Ro'yxatdagi sonlar yig'indisi {sum(juft_sonlar)} ga teng.")
print(f"{max(juft_sonlar)} - {min(juft_sonlar)} = {max(juft_sonlar) - min(juft_sonlar)}")
print(len(juft_sonlar))
print(juft_sonlar[:20])
print(juft_sonlar[-20:])
print(juft_sonlar[250:270])
'''

taomlar = ["Palov", "Pizza", "Sho'rva", "Manti", "Do'lma"]
nonushta = taomlar[:]
nonushta.remove("Pizza")
nonushta.remove("Manti")
nonushta.append("Bo'g'irsoq")
nonushta.append("Shirchoy")
del nonushta[0]
print(taomlar)
print(nonushta)

nonushta =tuple(nonushta)
print(nonushta)
