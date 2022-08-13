# 28-dars: KLASSLAR 
# Sana: 13/08/2022
# Muallif: Nozimjon Nabiev

class User:
    """Foydalanuvchi ma'lumotlarini qabul qiluvchi klass"""
    
    def __init__(self, foydalanuvchi, ism, email, yosh):
        self.user = foydalanuvchi
        self.name = ism
        self.email = email
        self.age = yosh

    def get_info(self):
        return f"Foydalanuvchi:{self.user}, ismi: {self.name}, email: {self.email} "
    
    def t_yili(self, joriy_yil):
        return joriy_yil - self.age
    
    def age_limit(self):
        if self.age < 18:
            return "Access denied!"
        else:
            return f"Access granted! Welcome {self.name}!"

user1 = User("anvar444", "Anvar Hoshimov", "anvar456@gmail.com", 25)
user2 = User("sobir45", "Sobir Botirov", "sobirbotirov@gmail.com", 16)
user3 = User("jahongir000", "Jahongir Qosimov", "qosimov@gmail.com", 10)
print(user1.age_limit())