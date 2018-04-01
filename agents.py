class Agent:
    def __init__(self, world):
        self.world = world
        print ('Agent base is born')
        
    def act(self, action, **kwarg):
        try:
            action(**kwarg)
        except NotImplementedError:
            print ('The action cannot be fulfilled. Looking for solution...')
            self.look('notify')
            
    def look(self, goal):
        for agent in self.world:
            if agent.goal == goal:
                print ('Agent {} could served the {} goal.'.format(agent.name, goal))
                agent.serve(goal)
                
    def serve(self, goal):
        service = getattr(self, goal)
        if service is not None:
            service()
            
    
    
class Reminder (Agent):
    def __init__(self, world):
        super().__init__(world)
        print('Reminder is born')
        self.name = 'reminder'
        self.bonded = []
        self.intention = 'to store reminders' #check SPARK: http://www.ai.sri.com/~spark/doc/SparkInANutshell.html
        self.belief = 'none'
        self.goal = 'remind'
        self.plan = { 
            'notify':'create_reminder', 
            'message': True,
            'time': True
        }
        self.reminder_time=''
        self.reminder_message=''
    
    def create_reminder(self, time, message):
        self.reminder_time = time
        self.reminder_message = message
        
    def step(self): 
        if self.reminder_time == 'today':
            self.act(self.notify)#, self.reminder_message)
            
    def notify(self):#, message):
        raise NotImplementedError
        
        #print('notified {} with message: {}'.format(address, message))
    
class Notify(Agent):
    def __init__(self, world):
        super().__init__(world)
        self.name = 'Notify'
        print('Notify is born')
        self.bonded = []
        self.intention = 'to notify user' #check SPARK: http://www.ai.sri.com/~spark/doc/SparkInANutshell.html
        self.belief = 'none'
        self.goal = 'notify'
        self.plan = { 
            'notify':'notify_action', 
            'message': True,
            'address': True
        }
    
    def notify(self, address='@', message='hello'):
        print('notified {} with message: {}'.format(address, message))
    

class Dummy(Agent):
    def __init__(self, world):
        super().__init__(world)
        self.name = 'Dummy'
        print('Dummy is born')
        self.bonded = []
        self.intention = 'to notify user' #check SPARK: http://www.ai.sri.com/~spark/doc/SparkInANutshell.html
        self.belief = 'none'
        self.goal = 'print'
        self.plan = { 
            'notify':'print_action', 
            'param': True,
        }
    
    def print_(self, param):
        print(param)
    