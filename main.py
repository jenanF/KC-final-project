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
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.tabbedpanel import TabbedPanel

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

class EducatScreen(Screen):
    pass

class BritishAirwaysScreen(Screen):
    pass
    #def show(self):
       # datePicker = MDDatePicker(year=2023,month=9,day=13)
        #datePicker.open()

class UniUkScreen(Screen): 
    pass

class OxfordScreen(Screen):
    oxftext = '''The University of Oxford is a collegiate research university in Oxford, England.There is evidence of teaching as early as 1096,making it the oldest university in the English-speaking world and the world's second-oldest university in continuous operation.It grew rapidly from 1167 when Henry II banned English students from attending the University of Paris.After disputes between students and Oxford townsfolk in 1209, some academics fled north-east to Cambridge where they established what became the University of Cambridge.The two English ancient universities share many common features and are jointly referred to as Oxbridge. The university is made up of thirty-nine semi-autonomous constituent colleges, four permanent private halls, and a range of academic departments which are organised into four divisions.All the colleges are self-governing institutions within the university, each controlling its own membership and with its own internal structure and activities. All students are members of a college. It does not have a main campus, and its buildings and facilities are scattered throughout the city centre. Undergraduate teaching at Oxford consists of lectures, small-group tutorials at the colleges and halls, seminars, laboratory work and occasionally further tutorials provided by the central university faculties and departments. Postgraduate teaching is provided in a predominantly centralized fashion. Oxford operates the Ashmolean Museum, the world's oldest university museum; Oxford University Press, the largest university press in the world; and the largest academic library system nationwide.In the fiscal year ending 31 July 2022, the university had a total consolidated income of £2.78 billion, of which £711.4 million was from research grants and contracts. Oxford has educated a wide range of notable alumni, including 30 prime ministers of the United Kingdom and many heads of state and government around the world.As of October 2022, 73 Nobel Prize laureates, 4 Fields Medalists, and 6 Turing Award winners have matriculated, worked, or held visiting fellowships at the University of Oxford, while its alumni have won 160 Olympic medals. Oxford is the home of numerous scholarships, including the Rhodes Scholarship, one of the oldest international graduate scholarship programmes.'''



class ScreenManager(ScreenManager):
    pass

class MyAppApp(App):
    pass


MyAppApp().run()