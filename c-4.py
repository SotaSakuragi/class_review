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

    def info_csv(self):
        self.csv = self.name + "," + str(self.age) + "," + str(self.money)
        return self.csv


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す
print(ken.info_csv())

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.info_csv()  # "Tom Ford,57,1500" という値を返す
print(tom.info_csv())

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
print(ieyasu.info_csv())
