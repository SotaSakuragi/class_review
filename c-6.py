class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.family_name

    def entry_fee(self):
        if self.age <= 3:
            return "無料"
        elif self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 65 <= self.age < 75:
            return 1200
        else:
            return 500

    def info_csv(self):
        csv_string = self.full_name() + "," + str(self.age) + "," + str(self.entry_fee())
        return csv_string


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す
print(ken.entry_fee())

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.entry_fee()  # 1500 という値を返す
print(tom.entry_fee())

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee()  # 1200 という値を返す
print(ieyasu.entry_fee())

souta = Customer(first_name="souta", family_name="sakuragi", age=3)
ieyasu.entry_fee()  # 無料 という値を返す
print(souta.entry_fee())

tubasa = Customer(first_name="tubasa", family_name="matidera", age=75)
ieyasu.entry_fee()  # 500 という値を返す
print(tubasa.entry_fee())
