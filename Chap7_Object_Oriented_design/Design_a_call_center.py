# Call Center:  Imagine you have a call center with three levels of employees: Respondent,
# manager, and director. An incoming telephone call must be first allocated to a respondent who is free.
# if the responder can't handle the call, he or she must escalate the call to a manager.
# if the manager is not free or not able to handle it, the the call should be escalated to a director. Design the classes and datastructures
# for this problem. Implement a method dispatchCall() which assigns a call to the first 
# available employee.

class CallCenter(): # are the parantheses necessary?
    def __init__(self, respondents, managers, director):
        self.respondents = respondents
        self.managers = managers
        self.director = director
        self.respondent_queue = []
        self.call_queue = []
        for respondent in respondents:
            respondent.callcenter = self  # not sure why 
            if not respondent.call:
                self.respondent_queue.append(respondent)

    def route_respondent(self, respondent):
        if len(self.call_queue):
            respondent.take_call(self, call_queue.pop())
        else:
            self.respondent_queue(respondent)


    def route_call(self, call):
        if len(self.respondent_queue):
            self.respondent_queue.pop(0).take_call
        else:
            self.call_queue.append(call)


class Call():
    def __init__(self, issue):
        self.issue = issue
        self.employee = None

    def resolve(self, handled):
        if handled:
            self.issue = None
        self.employee = None


    def apologize_and_hangup(self):
        # Try calling our competitor
        self.employee = None

    class Employee(object):
        def __init__(self, name, manager):
            self.name = name
            self.manager = manager
        
        def take_call(self,call):
            if self.call:
                self.escalate(call)
            else:
                self.call = call
                self.call.employee = self  # why ?

        def escalate(self, call):
            if self.manager: 
                self.manager.take_call(call)
            else:
                call.apologize_and_hangup

        def finish_call(self, handled = True):
            if not handed:
                if self.manager:
                    self.manager.take_call(self.call)
                else:
                    call.apologize_and_hangup()
            self.call = None

    class manager(Employee):
        pass  

    class Director(Employee):
        def __init__(self, name):
            super(Director,self).__init__(name, None)  # why ? 

            




