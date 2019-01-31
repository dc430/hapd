import kivy


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

class NavScreen(Screen):
    pass

class NewUser(Screen):
    pass

class ExistingUser(Screen):
    pass

class HomePage(Screen):
    pass

class UserScreenManager(ScreenManager):
    pass

frontEnd = Builder.load_file('style.kv')

class Main(App):
    def build(self):
        return frontEnd

if __name__ == '__main__':
    Main().run()




