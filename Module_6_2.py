class Vehicle:
    def _init_(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        if (color.lower() in variant.lower() for variant in self.__COLOR_VARIANTS):
            self.__color = color
        else:
            self.__color = self.__COLOR_VARIANTS[0]

    __COLOR_VARIANTS = ["black", "white", "red", "green", "blue"]

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        print(f"model: {self.get_model()}, horse power: {self.__engine_power()}, color: {self.get_color()}, owned by: {self.owner}")

    def set_color(self, new_color):
        if (new_color.lower() in variant.lower() for variant in self.__COLOR_VARIANTS)):
            self.new_color = new_color
        else:
            return print(f"Нельзя сменить цвет на {new_color}")




class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5
    pass

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500,'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()

print(vehicle1.owner)

