from agents import Notify
from agents import Dummy
from agents       import Reminder



world = []
reminder = Reminder(world)
world.append(reminder)
world.append(Notify(world))
world.append(Dummy(world))
    
reminder.create_reminder('today','visit the doctor')
reminder.step()

