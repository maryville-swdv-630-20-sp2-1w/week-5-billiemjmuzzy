from abc import ABCMeta, abstractmethod

class LeaveManagement(metaclass=ABCMeta):
   def __init__(self, id, name, hours, accrued, taken):
       self.id = id
       self.name = name
       self.hours = hours
       self.accrued = accrued
       self.taken = taken
       
   @abstractmethod
   def get_leave_type(self):
         pass
     
   def add_hours(self, accrued):
        """
        Method to increment hours available
        to request
        Returns hours accrued and hours available
        """
        self.accrued += accrued
        self.hours += accrued
        return self.accrued, self.hours
     
   def __str__(self):
        """
        Method to return details of leave
        """
        return f'{"*"*50}\n{self.get_leave_type().upper().center(50)}\n{"*"*50}\nEmployee ID: {self.id}\nEmployee Name: {self.name[0]} {self.name[1]}\nAvailable: {self.hours}\n'
    
class PaidTimeOff(LeaveManagement):
    def get_leave_type(self):
        return "Paid Time Off"
    
class FlexTime(LeaveManagement):
    def get_leave_type(self):
        return "Flex Time"

    
    
class LeaveManagementFactory(object):
    @classmethod
    def create(cls, name, *args):
        name = name
        
        if name == 'paid time off':
            return PaidTimeOff(*args)
        elif name == 'flex time':
            return FlexTime(*args)
  
        
        
        
if __name__ == "__main__":
    
   lm = LeaveManagementFactory.create("paid time off", 1234, ("Billie", "Muzzy"), 5, 0, 0)
   lm.add_hours(3)
   print(lm)
   
   lm2 = LeaveManagementFactory.create("flex time", 1234, ("Billie", "Muzzy"), 10, 0, 0)
   lm2.add_hours(20)
   print(lm2)
  
    
