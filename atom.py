from abc import ABC, abstractmethod

class Atom (ABC):
    
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def get_outer_electron(self):
        pass
    
    @abstractmethod
    def can_bond(self):
        pass
    
    @abstractmethod
    def give_electron(self):
        pass
    
    @abstractmethod
    def take_electron(self):
        pass
    
    @abstractmethod
    def process(self):
        pass