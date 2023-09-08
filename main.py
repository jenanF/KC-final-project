from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

Window.size = (400, 630)
Window.clearcolor= "4b548b"

class MainWidget(Widget):
    pass

class MyAppApp(App):
    pass

def on_toggle_active(self):
    print("hello")


MyAppApp().run()