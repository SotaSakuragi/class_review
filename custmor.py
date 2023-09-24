class Customer:
    def __init__(self, first_name, family_name, age):
        self.name = first_name + " " + family_name
        self.age = age

    def full_name(self):
        return self.name


"""
ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す
print(ken.full_name())

tom = Customer(first_name="Tom", family_name="Ford")
tom.full_name()  # "Tom Ford" という値を返す
print(tom.full_name())
"""

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.age  # 15 という値を返す
print(ken.age)

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.age  # 57 という値を返す
print(tom.age)

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.age  # 73 という値を返す
print(ieyasu.age)
