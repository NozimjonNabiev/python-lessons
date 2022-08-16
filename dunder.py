# 32-dars: DUNDER METODLAR
# Sana: 15/08/2022
# Muallif: Nozimjon Nabiev

from uuid import uuid4

class Shaxs:
    __odamlar_soni = 0
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        self.tyil = tyil
        Shaxs.__odamlar_soni += 1
    
    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni
        
    def __repr__(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f" {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    def get_passport(self):
        return self.__passport
        

class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil,bosqich):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = uuid4()
        self.bosqich = bosqich
        self.subjects = []
        Talaba.__talabalar_soni += 1
    
    @classmethod
    def get_student_num(cls):
        return cls.__talabalar_soni
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.__idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def set_bosqich(self, new_bosqich):
        self.bosqich = new_bosqich
    
    def __lt__(self, boshqa_talaba):
        if isinstance(boshqa_talaba, Talaba):
            return self.bosqich > boshqa_talaba.bosqich
    
    def __eq__(self, new_talaba):
        if isinstance(new_talaba, Talaba):
            return self.bosqich == new_talaba.bosqich
            
    def __repr__(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.tyil}-yilda tug`ilgan"
        return info
        
    def fanga_yozil(self, fan):
            return self.subjects.append(fan)
        
    def remove_fan(self, fan):
        if fan in self.subjects:
            return self.subjects.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz!"
     
     
class Fan:
    """Talabalar yozilgan fanlar uchun klass"""
    def __init__(self, nomi):
        self.name = nomi
        self.talabalar_list = []
     
    def __repr__(self):
        info = f"Fan nomi: {self.name.title()}\nO'qiyotgan talabalar:{self.talabalar_list}"
        return info
    
    def add_student(self, *talabalar):
        for talaba in talabalar:
            if isinstance(talaba, Talaba):
                self.talabalar_list.append(talaba)
            else:
                print("Bu talaba haqida ma'lumot mavjud emas")
    
    def __getitem__(self, index):
        if isinstance(index, int):
            return self.talabalar_list[index]    
    
    def __setitem__(self, index, qiymat):
        if isinstance(qiymat, Talaba):
            self.talabalar_list[index] = qiymat
    
    def __len__(self):
        return len(self.talabalar_list)
     
    def __add__(self, talaba):
        if isinstance(talaba, Talaba):
            self.talabalar_list.append(talaba)  
    
    def __call__(self, *talabalar):
        for talaba in talabalar:
            if isinstance(talaba, Talaba):
                self.talabalar_list.append(talaba)
            else:
                print("Bu talaba haqida ma'lumot mavjud emas")
    
    def __sub__(self, talaba):
        if isinstance(talaba, Talaba):
            self.talabalar_list.remove(talaba)
     

shaxs1 = Shaxs("Asror", "Valiyev", "AC4554854", 1996)
shaxs2 = Shaxs("Qodir", "Samandarov", "AA100255", 1999)
shaxs3 = Shaxs("Javlon", "Ahmadov", "AB78852520", 2002)


talaba1 = Talaba("Hojimat", "Erkinov", "AC55645440", 2001, 2)
talaba2 = Talaba("Jaloliddin", "Toshmatov", "AB0784454", 2003, 1)
talaba3 = Talaba("Gulchiroy", "Asadova", "AA5564540", 2002, 3)
talaba4 = Talaba("Asaloy", "Kamolova", "AA5444789", 2002, 2)
talaba5 = Talaba("Asilbek", "Eshonqulov", "AC56450000", 1999, 4)
talaba6 = Talaba("Behzod", "Jamolov", "AB999004444", 2003, 1)
talaba7= Talaba("Gulasal", "Karimova", "AC45454000", 2002, 3)
talaba8 = Talaba("Nigina", "Nosirova", "AB56641433", 2004, 1)

algebra = Fan("Algebra")
geometry = Fan("Geometry")
english = Fan("English")
it = Fan("IT")

algebra.add_student(talaba1,talaba2,talaba3)
geometry.add_student(talaba4,talaba5)
english.add_student(talaba7,talaba8)
it+talaba6