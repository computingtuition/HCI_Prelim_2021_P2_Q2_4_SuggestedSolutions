### NOTE: you will need to import the object(s) you need
### from the previous tasks' files
from TASK2_2 import ServiceRecord

class AppServiceRecord(ServiceRecord):

    ### no need to override __init__ since all attributes remain the same

    def getAppType(self):
        if self.AppType == 'WA':
            return 'WHATSAPP'
        elif self.AppType == 'FB':
            return 'FACEBOOK MESSENGER'
    
    def getSuccess(self):
        # use self. to trigger functions from same / parent class
        if self.isSuccess():
            return 'SUCCESS'
        else:
            return 'FAILED'


class SmsServiceRecord(ServiceRecord):

    ### no need to override __init__ since all attributes remain the same

    def getAppType(self):
        return 'SHORT MESSAGE SERVICE'
    
    def getSuccess(self):
        # use self. to trigger functions from same / parent class
        if self.isSuccess():
            return 'SUCCESS'
        else:
            return 'FAILED'