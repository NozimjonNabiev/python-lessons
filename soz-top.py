# 26-dars: So'z topish o'yini
# Sana: 12/08/2022
# Muallif: Nozimjon Nabiev

import random
from uzwords import words

def get_words():
    tasodifiy_soz = random.choice(words)
    return tasodifiy_soz.upper()
        
soz = get_words()
uzunlik = len(soz) 
yashir = []
print(f"Мен {uzunlik} хонали сўз ўйладим. Топа оласизми?")
for i in range(uzunlik):
    yashir.append('-')
    
def display():
    user_letters = [] 
    count = 0
    while '-' in yashir:
        count += 1
        print(*yashir)
        harf = input("Ҳарф киритинг: ").upper()
        if harf in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
        else:
            user_letters.append(harf)
        
            if harf not in soz:
                print("Бундай ҳарф йўқ.")
            else:
                    print(f"{harf} ҳарфи тўғри.")
        print("Шу вақтгача киритган ҳарфларингиз: " , *user_letters)
        
        
        for i in range(len(yashir)):
            if soz[i] == harf:
                yashir[i] = harf
    
    return count
            
test = display()

print(f"Табриклайман! {soz.upper()} сўзини {test} та уринишда топдингиз.")

    