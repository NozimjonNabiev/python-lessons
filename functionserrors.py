# 36-dars: FUNKSIYANI TEKSHIRISH
# Sana: 16/08/2022
# Muallif: Nozimjon Nabiev

def eng_kattasi(x,y,z):
    if x>y and x>z:
        return z
    elif y>x and y>z:
        return y
    else:
        return z

# x = eng_kattasi(10,20,30)
# print(x)

def capital_letter(list_letters):
    new_list = []
    for word in list_letters:
        word = word.title()
        new_list.append(word)
    return new_list

# test = ['asal', 'shirin', 'dilnoza', 'kamola']
# print(capital_letter(test))


def even_numbers(sonlar):
    even_nums = []
    for son in sonlar:
        if son%2==0:
            even_nums.append(son)
    return even_nums 

# sonlar = [10,11,17,19,21,100,20,45,40]
# test2 = even_numbers(sonlar)
# print(test2)
            

def fibonacci_nums(num, sonlar = list(range(100))):
    fibonacci_numbers = []
    for son in sonlar:
        if son == 0:
            fibonacci_numbers.append(0)
        elif son == 1:
            fibonacci_numbers.append(1)
        else:
            fibonacci_numbers.append(fibonacci_numbers[son-1] + fibonacci_numbers[son-2]) 
    if num in fibonacci_numbers:
        return True
    else:
        return False

# test = fibonacci_nums(4)
# print(test)