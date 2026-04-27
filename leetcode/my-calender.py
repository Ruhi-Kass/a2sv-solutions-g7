class MyCalendar:

    def __init__(self):
        self.events = [] 
    def book(self, startTime: int, endTime: int) -> bool:
        
        for s, e in self.events:
            
            if max(startTime, s) < min(endTime, e):
                return False
        
        
        self.events.append((startTime, endTime))
        self.events.sort(key=lambda x: x[0])  
        return True
