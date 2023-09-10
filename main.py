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
from kivy.properties import ListProperty, StringProperty

Window.size = (400, 630)
Window.clearcolor= "4b548b"

class MainWidget(Screen):
    pass


class UkScreen(Screen):
    pass


currencies = requests.get("https://www.bloomberg.com/markets/currencies")

def currncy(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
   # test = soup.find('tbody', {'class' : 'data-table-body'}).text
   # title_curncy = soup.find('th', {'class' : 'data-table-headers-cell'}).text
   # print(title_curncy)
    #print(test.__len__())


currncy(currencies)


class CurrnciesScreen(Screen):
    src = currencies.content
    soup = BeautifulSoup(src, "lxml")
    #test = soup.find('tbody', {'class' : 'data-table-body'}).text
   # title_curncy = StringProperty(soup.find('th', {'class' : 'data-table-headers-cell'}).text)
   # title_value = soup.find_all('tr', {'class' : 'data-table-headers'})[0].children
   # print(title_value)

class ConvertorScreen(Screen):
    pass
   # from_ = "USD"
    #to_ = "EUR"
    #amount = 0
    #convert = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_}&to={to_}")
    #print(f"{amount}  {from_} is {convert.json()['rates'][to_]}  {to_}")

class AirwaysScreen(Screen):
    pass

class LocationsScreen(Screen):
    pass




class ScreenManager(ScreenManager):
    pass

class MyAppApp(App):
    pass


MyAppApp().run()