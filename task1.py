
class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def update_owner(self, new_owner):
            self.owner = new_owner
            print(f"Owner updated to: {self.owner}") # updates the owner of vehicle

vehicle = Vehicle("A123", "Chevy", "Roger")
print(vehicle)
vehicle_owner = Vehicle("R345", "Dodge", input("New owner name: ")) # allows user to update owner
print(vehicle_owner)
