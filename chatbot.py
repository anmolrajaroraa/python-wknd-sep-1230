from datetime import datetime

helloIntent = ["hello", "hi", "hey", "namaste"]
timeIntent = ["time please", "what's the time"]
dateIntent = ["date please", "what's the date"]

while True:
    userMessage = input("Enter message: ")
    # for msg in helloIntent:
    #     if msg == userMessage:
    #         print("Hi")
    if userMessage in helloIntent:    #membership operator
        print("hi")
    elif userMessage in dateIntent:
        now = datetime.now()
        print(now.strftime("%D"))
    elif userMessage in timeIntent:
        now = datetime.now()
        print(now.strftime("%a %d %b %H:%M:%S %p"))
    elif userMessage == "bye":
        print("see you later")
    else:
        print("I don't understand !")






'''
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2020, 1, 5, 14, 48, 50, 198978)
>>> datetime.now()
datetime.datetime(2020, 1, 5, 14, 49, 7, 827151)
>>> datetime.now()
datetime.datetime(2020, 1, 5, 14, 49, 12, 557720)
>>> now = datetime.now()
>>> now.strftime("%y")
'20'
>>> now.strftime("%Y")
'2020'
>>> now.strftime("%m")
'01'
>>> now.strftime("%M")
'49'
>>> now.strftime("%H")
'14'
>>> now.strftime("%S")
'36'
>>> now.strftime("%s")
'1578215976'
>>> now.strftime("%a")
'Sun'
>>> now.strftime("%A")
'Sunday'
>>> now.strftime("%p")
'PM'
>>> now.strftime("%d")
'05'
>>> now.strftime("%D")
'01/05/20'
>>> now.strftime("%b")
'Jan'
>>> now.strftime("%B")
'January'
>>> now.strftime("%a %d %b %H:%M:%S %p")
'Sun 05 Jan 14:49:36 PM'

message = "open google"
>>> mesaage = message.split()
>>> message
'open google'
>>> mesaage = message.split(' ')
>>> message = message.split()
>>> message
['open', 'google']
>>> webbrowser.open("https://" + message[1] + ".com")
True
>>> import os
>>> os.getcwd()
'/Users/anmolrajarora/Documents'
>>> #get current working directory
>>> os.chdir('/Users/anmolrajarora/Documents/AdvPython')    #change directory
>>> os.getcwd()
'/Users/anmolrajarora/Documents/AdvPython'
>>> os.listdir()
['07-SocialNetwork_Part-3.wmv', '06-SocialNetwork_Part-2.wmv', '02-OOPS+MVC+DB.wmv', '03-WebIntegration.wmv', '04-OnlineShop_Part-1.wmv', '01-OOPS.wmv', '08-SocialNetwork_Part-4.wmv', '10-DesktopApp_Part-1.wmv', '09-SocialNetwork_Part-5.wmv', '05-SocialNetwork_Part-1.wmv']
>>> print("Dwayne \"Rock\" Johnson")
Dwayne "Rock" Johnson
>>> print("Dwayne \Rock\ Johnson")
Dwayne \Rock\ Johnson
>>> print("Dwayne \\Rock\\ Johnson")
Dwayne \Rock\ Johnson
>>> os.chdir('C:\\Users\\Navin Bansal\\Downloads')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    os.chdir('C:\\Users\\Navin Bansal\\Downloads')
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Navin Bansal\\Downloads'
>>> os.startfile('whatsapp-image-123.jpg')
'''