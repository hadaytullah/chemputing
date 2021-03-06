from atom import Atom

class Oxygen(Atom):
    def __init__(self):
        super().__init__()
        print('Oxygen born')
        self.bonded = []
        self.outer_e = 1
        self.give_e = 1
        self.take_e = 1
    
    def get_outer_electron():
        return sef.outer_e
    
    def can_bond(self, atom):
        if atom.give_e > self.take_e or atom.take_e < self.give_e:
            return True
        return False
    
    def give_electron(self):
        return self.give_e
    
    def take_electron(self):
        return self.take_e
    
    def bond(self, atom, e):
        self.outer_e += e    
        self.bonded.append(atom)
        
    def process(self, value):
        if len(self.bonded) > 0:
            for atom in self.bonded:
                value = atom.process(value)
        return value/5 #just a dummy process