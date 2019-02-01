import kivy


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class NavScreen(Screen):
    pass

class NewUser(Screen):
    pass

class ExistingUser(Screen):
    def __init__(self, **kwargs):
        super(ExistingUser, self).__init__(**kwargs)
    
    def sendId(self, id, pin):
        print(id+' '+pin)


class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
    

class firebase(Screen):
    def __init__(self, **kwargs):
        super(firebase, self).__init__(**kwargs)
        self.gender = None
    def sendDataToRealTimeDb(self, name, age, dob, pin):
        #start writing here - poojitha
        print(name, age, dob, pin, self.gender)


    
    


    
class UserScreenManager(ScreenManager):
    pass

frontEnd = Builder.load_file('style.kv')

class Main(App):
    def build(self):
        return frontEnd

if __name__ == '__main__':
    Main().run()




