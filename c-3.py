class Customer:
    def __init__(self, first_name, family_name, age):
        self.name = first_name + " " + family_name
        self.age = age

        if age < 20:
            self.money = 1000
        elif 20 <= age < 65:
            self.money = 1500
        elif 65 <= age:
            self.money = 1200

    def full_name(self):
        return self.name

    def entry_fee(self):
        return self.money


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す
print(ken.entry_fee())

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.entry_fee()  # 1500 という値を返す
print(tom.entry_fee())

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee()  # 1200 という値を返す
print(ieyasu.entry_fee())
