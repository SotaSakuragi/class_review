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

    def info_pipe(self):
        # ここにあったcsvかな？
        string = self.full_name() + "  " + str(self.age) + "  " + str(self.entry_fee())
        return string


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_pipe()  # "Ken Tanaka|15|1000" という値を返す
print(ken.info_pipe())

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.info_pipe()  # "Tom Ford|57|1500" という値を返す
print(tom.info_pipe())

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_pipe()  # "Ieyasu Tokugawa|73|1200" という値を返す
print(ieyasu.info_pipe())
