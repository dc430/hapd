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
#Config.set('graphics', 'width', '700')
#Config.set('graphics', 'height', '700')
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
#----------------------- End --------------------------------#

class NavScreen(Screen):
    def __init__(self, **kwargs):
        super(NavScreen, self).__init__(**kwargs)
        with open('quotes.json') as f:
            data = json.load(f)
        self.quote = str(data[str(random.randint(1,5))])
        

class NewUser(Screen):
    def __init__(self, **kwargs):
        super(NewUser, self).__init__(**kwargs)
        self.status = status
        self.nE = name_error
        self.pE = pin_error
        self.aE = age_error

    ErrorAge = StringProperty('')
    erAge = ObjectProperty()
    def update_status(self):
        self.status = status
        self.nE = name_error
        self.pE = pin_error
        self.aE = age_error

class ExistingUser(Screen):
    def __init__(self, **kwargs):
        super(ExistingUser, self).__init__(**kwargs)
    
    def sendId(self, id, pin):
        print(id+' '+pin)

class api(Screen):
    def __init__(self, **kwargs):
        super(api, self).__init__(**kwargs)
        self.gender = None
        
    def sendDataToRealTimeDb(self, name, age, dob, pin):
        global active, status, age_error, name_error, pin_error
        active = 1
        temp = str(age)
        if (temp.isnumeric() == False):
            age_error = 1
            status = 0
        if (name == None):
            name_error = 2
            status = 0
        if(len(str(pin)) < 6):
            pin_error = 1
            status = 0
        if(pin == None):
            pin_error = 2
            status = 0

        data = {'name': name, 'age': age, 'gender': self.gender, 'dob': dob, 'pin': pin}
        data = json.dumps(data)
        headers = {'Authorization' : '', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
        url = 'https://hapdwebhook.herokuapp.com/webhook'
        r = requests.post(url, data=data, headers=headers)
        #r.text contains the dictionary/json file with the response from webhook
        print(r.text)
    
class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        

    


    
class UserScreenManager(ScreenManager):
    pass

frontEnd = Builder.load_file('style.kv')

class Main(App):
    def build(self):
        return frontEnd

if __name__ == '__main__':
    Main().run()




