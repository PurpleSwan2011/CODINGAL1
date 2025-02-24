class Dog:
    species = "Canis familiaris"

    def __init__(self, breed, name):
        # Instance variables
        self.breed = breed
        self.name = name

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")

dog1 = Dog("Golden Retriever", "Buddy")
dog2 = Dog("German Shepherd", "Max")

print("Details of Dog 1:")
dog1.display_details()
print("\nDetails of Dog 2:")
dog2.display_details()
