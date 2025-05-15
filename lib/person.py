#!/usr/bin/env python3

class Person:
    # Instance method: talk
    def talk(self):
        print("Hello World!")

    # Instance method: walk
    def walk(self):
        print("The person is walking.")

# Optional test code (only runs when you execute this file directly)
if __name__ == "__main__":
    alice = Person()
    alice.talk()   # Should print: Hello World!
    alice.walk()   # Should print: The person is walking.
