#!/usr/bin/env python3

class Dog:
    # Instance method: bark
    def bark(self):
        print("Woof!")

    # Instance method: sit
    def sit(self):
        print("The dog is sitting.")

# Optional test code (only runs when you execute this file directly)
if __name__ == "__main__":
    fido = Dog()
    fido.bark()  # Should print: Woof!
    fido.sit()   # Should print: The dog is sitting.
