from hydrogen import Hydrogen
from oxygen import Oxygen

Hx = Hydrogen()
Hy = Hydrogen()
O = Oxygen()

# NOTE: H and O could be agents existing is a space
# When they come in close proximity they bond based on
# their properties. Use MESA library.

if O.can_bond (Hx):
    O.bond (Hx,2)

print (O.process(10))