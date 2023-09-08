import requests
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

Window.size = (400, 630)
Window.clearcolor= "4b548b"

class MainWidget(Screen):
    pass


class UkScreen(Screen):
    pass



class ScreenManager(ScreenManager):
    pass

class MyAppApp(App):
    pass

def on_toggle_active(self):
    print("hello")


MyAppApp().run()