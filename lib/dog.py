#!/usr/bin/env python3

class Dog:
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name
        
        else:
            print(f'Name must be string between 1 and 25 characters.')
    
    name = property(get_name, set_name)
    
    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
        if breed in approved_breeds:
            self._breed = breed
        
        else:
            print(f"Breed must be in list of approved breeds.")
    
    breed =  property(get_breed, set_breed)