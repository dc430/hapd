import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ObjectProperty
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '700')
#For heroku
from kivy.network.urlrequest import UrlRequest
import urllib
import requests
import json
import random
#---------------------- Error Global Variables --------------#
active = 0
status = 1
age_error = 0
gender_error = 0
name_error = 0
pin_error = 0
dob_error = 0
currentPID = 0
#----------------------- End --------------------------------#

class NavScreen(Screen):
    def __init__(self, **kwargs):
        super(NavScreen, self).__init__(**kwargs)
        with open('data.json') as f:
            data = json.load(f)
        self.quote = str(data["quotes"][str(random.randint(1,5))])
        

class NewUser(Screen):
    def __init__(self, **kwargs):
        super(NewUser, self).__init__(**kwargs)
        self.status = status
        self.nE = name_error
        self.pE = pin_error
        self.aE = age_error
        self.dE = dob_error
        self.gE = gender_error
        self.temp = str('Hello')

    def update_status(self):
        self.status = status
        self.nE = name_error
        self.pE = pin_error
        self.aE = age_error
        self.dE = dob_error
        self.gE = gender_error


class ExistingUser(Screen):
    def __init__(self, **kwargs):
        super(ExistingUser, self).__init__(**kwargs)
    
    def checkCredentials(self, pId, pin):
        global currentPID
        data = {
            "pId": pId,
            "pin": pin
        }
        data = json.dumps(data)
        headers = {'Authorization' : '', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
        url = 'https://api-hapd.herokuapp.com/checkLogin'
        r = requests.post(url, data=data, headers=headers)
        print(r.text, type(r.text))


class api(Screen):
    def __init__(self, **kwargs):
        super(api, self).__init__(**kwargs)
        self.gender = None
        
    def sendDataToRealTimeDb(self, name, age, dob, pin, mB, fB):
        global active, status, age_error, name_error, pin_error, dob_error, gender_error
        age_error = name_error = pin_error = gender_error = dob_error = 0
        status = 1
        active = 1
        temp = str(age)
        if(mB.status == False and fB.status == False):
            self.gender = None
        if (temp.isnumeric() == False):
            age_error = 1
            status = 0
        if (str(age) == ''):
            age_error = 2
            status = 0
        if (str(name) == ''):
            name_error = 2
            status = 0
        if(len(str(pin)) > 4 or len(str(pin)) < 4):
            pin_error = 1
            status = 0
        if(str(pin) == ''):
            pin_error = 2
            status = 0
        if(str(dob) == ''):
            dob_error = 2
            status = 0
        if(self.gender == None):
            gender_error = 2
            status = 0 
        if(status == 1):
            data = {
                'name': name, 
                'age': age, 
                'gender': self.gender, 
                'dob': dob, 
                'pin': pin, 
            }
            data = json.dumps(data)
            headers = {'Authorization' : '', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
            url = 'https://api-hapd.herokuapp.com/addNewUser'
            try:
                r = requests.post(url, data=data, headers=headers)
            except:
                print("Couldn't send to webhook")
            print("Data from api:\n", r.text)
    
class tempPage(Screen):
    def __init__(self, **kwargs):
        super(tempPage, self).__init__(**kwargs)
        self.pId = "P1"
        
    
class UserScreenManager(ScreenManager):
    pass

frontEnd = Builder.load_file('kv/style.kv')

class Main(App):
    def build(self):
        return frontEnd

if __name__ == '__main__':
    Main().run()




