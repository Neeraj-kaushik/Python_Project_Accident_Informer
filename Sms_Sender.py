"""These file will help to import the the Impactinformer file and GetLocation file """
from subprocess import call
import uuid
import time

"""This is class for Impact Informer file and help to call the Impact Informer"""

class Impactinformer(object):
    
    def __init__(self,path='C:/Users/NEERAJ/Desktop/PythonProject/ImpactInformer.py'):
        self.path=path
        
    def call_Impactinformer(self):
        call(["Python","{}".format(self.path)])

"""This is class for GetLocation file and help to get location and store it to 1.html"""        
class Getlocation(object):
    
    def __init__(self,path='C:/Users/NEERAJ/Desktop/PythonProject/GetLocation.py'):
        self.path=path
        
    def call_Getlocation(self):
        call(["python","{}".format(self.path)])

"""This fumction is used to just check Messsage is sent or not"""
def Messege_Checker():
    print("Message sent and your location is found and stored in 1.html")

"""This is main function which will do all work.This is just outlook for messaging we can easily connect it to
Twilio, way2sms and other site."""        
if __name__=="__main__":
    
    Number=int(input("Enter your Family Phone Number "))
    
    """This is used to call getlocation and store it to 1.html"""
    
    g=Getlocation()
    g.call_Getlocation()
    
    """Thi is udes to call Impact informer """
    
    c=Impactinformer()
    c.call_Impactinformer()
    
    """This will generate a random id for message"""
    
    print('Your Msessage Id is ',' ',uuid.uuid1())
    
    print("Checking Message is sent or not and finding your location")
    
    """This is used to sleep the computer for particular time """
    time.sleep(6)
    Messege_Checker()