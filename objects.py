# 29-dars: OBYEKTLAR BILAN ISHLASH
# Sana: 13/08/2022
# Muallif: Nozimjon Nabiev

class Avto:
    def __init__(self, model, rang, korobka, narh, yil):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.yil = yil 
        self.kilometr = 0
    
    def get_info(self):
        return f"Mashina modeli {self.model}, rangi {self.rang}, {self.korobka} karobka, narxi {self.narh}$,{self.yil}-yil probeg {self.kilometr} km"
                
        
    def get_model(self):
        return self.model
    
    def get_color(self):
        return self.rang
    
    def get_korobka(self):
        return self.korobka
    
    def get_narh(self):
        return self.narh
    
    def get_yil(self):
        return self.yil
    
    def get_kilometr(self):
        return self.kilometr
    
    def update_kilometr(self, new_value):
        self.kilometr = new_value
        return self.kilometr
   
    
class Avtosalon:
    
    def __init__(self, nomi, manzili, mashinalar):
        self.name = nomi
        self.address = manzili 
        self.cars = mashinalar
        
        
    def get_info(self):
        return f"Avtosalon nomi: {self.name.title()} \nUshbu avtosalonda {self.cars} mashinalari sotuvda mavjud.\nManzili: {self.address}"
    
    def add_cars(self, car):
        self.cars.append(car)
        
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    
        
car1 = Avto("Malibu","qora", "avtomat", "40000", 2020)
car2 = Avto("Nexia3","oq", "mexanika", "25000", 2021)
car3 = Avto("Damas","oq", "mexanika", "15000", 2018)

car3.update_kilometr(10000)
print(car3.get_info())


avtosalon1 = Avtosalon("Chevrolet", "Mirzo Ulugbek St. 165A", ["Malibu","Nexia3", "Tracker", "Spark"])
avtosalon1.add_cars("Damas")


def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(avtosalon1))