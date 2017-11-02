
from datetime import datetime

class Call(object):
    num_of_calls = 0
    def __init__(self, caller_name, phone_number, reason_for_call):
        self.id = Call.num_of_calls
        self.caller_name = caller_name
        self.phone_number = phone_number
        self.call_time = datetime.now()
        self.reason_for_call = reason_for_call

        Call.num_of_calls += 1
    
    def display_info(self):
        print "ID: {}. Caller Name: {}. Phone Number: {}. Call Time: {}. Reason for Call: {}.".format(self.id, self.caller_name, self.phone_number, self.call_time, self.reason_for_call)
        return self
        

caller1 = Call( "Baka", "847-208-0883", "Need my Flask")
caller1.display_info()

class Center(object):
    def __init__(self, location, calls, queue_size):
        self.location = "Totally not located in India, Sahib."
        self.calls = calls
        self.queue_size