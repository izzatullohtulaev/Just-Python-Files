class Shaxs:
    def __init__(self, ism, familya, passport, tyil):
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil
    def get_info(self):
        return f"{self.ism} {self.familya}. Passport: {self.passport}. Tug'ilgan yili: {self.tyil}"
    def get_name(self):
        return self.ism
    def get_age(self, yil=2026):
        return yil-self.tyil
shaxs1 = Shaxs("Izzat", "Tulayev", "AA1234567", 2009)

class Talaba(Shaxs):
    def __init__(self, ism, familya, passport, tyil, idraqam):
        super().__init__(ism, familya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich

talaba1 = Talaba("Olim", "Mallayev", "AA9876543", 2007, "STD00034")