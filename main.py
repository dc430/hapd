import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

#For heroku
from kivy.network.urlrequest import UrlRequest
import urllib
import requests
import json
def bug_posted(req, result):
    print('Our bug is posted!')
    print(result)


class NavScreen(Screen):
    pass

class NewUser(Screen):
    pass

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




