"""In cars mainly when evr the accident occure airbags will be opened. 
These airbags work when they get signal from impact detector in car
(inbuilt). it will give four type of output to airbags and same outputs 
are used as an input which we are taking as user manual ."""

"""This function check the impact of accident and then tell to whom we 
have to send message"""

def ImpactDetector(n):
    switcher={
        0: "Minor Accident Occured Message will not sent to anyone",
        1: "Moderate Accident occured message will be sent to Police",
        2: "Serious Accident occured message will be sent to Police, Ambulance,Family memeber",
        3: "Very Serious Accident Occured message will be sent to Police, Ambulance,Family member"
    }
    return switcher.get(n,"No accident will Occure")

def Messenger(n):
    if n==0:
        print('Message is sent to No one as it is a minor accident')
    if n==1:
        print('Message and your location stored in 1.html are sent to Police as it is Moderate accident ')
    if n==2:
        print('Message and your location stored in 1.html are sent to Police, Ambulance and your Family Number as it is Serious Accident ')
    if n==3:
        print('Message and your location stored in 1.html are sent to Police, Ambulance and your Family Number as it is Very serious Accident') 
    
"""This function which will take output of impact detector as 
input in accident informer app"""

n=int(input("Enter the value of Impact Detector "))
print(ImpactDetector(n))
Messenger(n)
