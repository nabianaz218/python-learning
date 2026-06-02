# OOP allows us to model real-world concepts into code blueprints called Classes.

# 1. Base Class (Parent)
class Device:
    def __init__(self, brand, model):
        # Attributes unique to every instance
        self.brand = brand
        self.model = model
        self._power_on = False  # Protected attribute (convention hint)

    def turn_on(self):
        self._power_on = True
        return f"{self.brand} {self.model} is now powered up."


# 2. Inheritance (Child Class inheriting from Parent)
class Smartphone(Device):
    def __init__(self, brand, model, os):
        # Super() calls the constructor of the Parent Class to reuse its logic
        super().__init__(brand, model)
        self.os = os

    # 3. Polymorphism (Overriding parent method to exhibit unique behavior)
    def turn_on(self):
        # We modify the behavior specifically for Smartphones
        base_message = super().turn_on()
        return f"{base_message} Booting {self.os} operating system loading screen..."


# --- Instantiate Objects ---
generic_gadget = Device("GenericCorp", "X100")
print(generic_gadget.turn_on())

my_phone = Smartphone("Apple", "iPhone 15", "iOS")
print(my_phone.turn_on())  # Triggers the specialized polymorphic version