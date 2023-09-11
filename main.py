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
import webbrowser
import speech_recognition as sp
import pyttsx3




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

class OxfordScreen(Screen):#done
    oxftext = '''The University of Oxford is a collegiate research university in Oxford, England.There is evidence of teaching as early as 1096,making it the oldest university in the English-speaking world and the world's second-oldest university in continuous operation.It grew rapidly from 1167 when Henry II banned English students from attending the University of Paris.After disputes between students and Oxford townsfolk in 1209, some academics fled north-east to Cambridge where they established what became the University of Cambridge.The two English ancient universities share many common features and are jointly referred to as Oxbridge. The university is made up of thirty-nine semi-autonomous constituent colleges, four permanent private halls, and a range of academic departments which are organised into four divisions.All the colleges are self-governing institutions within the university, each controlling its own membership and with its own internal structure and activities. All students are members of a college. It does not have a main campus, and its buildings and facilities are scattered throughout the city centre. Undergraduate teaching at Oxford consists of lectures, small-group tutorials at the colleges and halls, seminars, laboratory work and occasionally further tutorials provided by the central university faculties and departments. Postgraduate teaching is provided in a predominantly centralized fashion. Oxford operates the Ashmolean Museum, the world's oldest university museum; Oxford University Press, the largest university press in the world; and the largest academic library system nationwide.In the fiscal year ending 31 July 2022, the university had a total consolidated income of £2.78 billion, of which £711.4 million was from research grants and contracts. Oxford has educated a wide range of notable alumni, including 30 prime ministers of the United Kingdom and many heads of state and government around the world.As of October 2022, 73 Nobel Prize laureates, 4 Fields Medalists, and 6 Turing Award winners have matriculated, worked, or held visiting fellowships at the University of Oxford, while its alumni have won 160 Olympic medals. Oxford is the home of numerous scholarships, including the Rhodes Scholarship, one of the oldest international graduate scholarship programmes.'''
    def openweb():
      webbrowser.open("https://goo.gl/maps/u7sv4fhHwx26Lpnd8")


class HotelsScreen(Screen):
    pass

class AvaitorHotelScreen(Screen):
    avatext = '''Aviator is an independent hotel for elite travellers moving between London and the world's leading destinations.

Located near London in Farnborough, Hampshire, Aviator opened in 2008 as one of the most striking design hotels in recent times. Innately stylish, Aviator binds the timeless glamour of aviation with seductive interiors and ultimate comfort.

The bedroom interiors are contemporary yet rich and comfortable with walnut panelling, leather accented furniture and bathrooms with black glass walls, granite vanity tops and chrome finishing. Sky Suites amplify the indulgent personality of the hotel with walk in wardrobes, generous bath tubs, Missoni blankets and space to lounge surrounded by dark wood Venetian blinds. Guests can discreetly access the fitness studio from their rooms using a guest only stairwell at the north end of the building.

The lobby and atrium of the hotel present One Eleven, the Brasserie and Sky Bar which overlooks the private Farnborough airport.

Within the Brasserie sit two of the hotel's private dining rooms, exemplifying the intimacy and allure of the dining experience. The variety of fresh and classical dishes are accompanied by carefully selected boutique wines from producers around the world.

Located on the first floor is Sky Bar, a cocktail bar designed with intention. Secluded black leather Rocket chairs and relaxing lounge areas create the ultimate place to sip our signature cocktails.

The design of event spaces at Aviator are well considered. The private entrance to the events wing and dedicated relaxing lounge areas provide direct access to the versatile meeting rooms. Used exclusively for tailored events and celebrations, the Sky Lounge overlooks awesome views of the airport and combines with the atrium to create a venue that promises to leave a lasting impression.'''


class TransportationScreen(Screen):
    pass

class CarsScreen(Screen):
    pass

class SiriScreen(Screen):
    pass
'''
    listener = sp.Recognizer()
    audio = pyttsx3.init()
    voices = audio.getProperty('voices')
    audio.setProperty('voice', voices[1].id)
    def sayit(text):
        audio = pyttsx3.init()
        audio.say(text)
        audio.runAndWait()
    try:
        with sp.Microphone() as source:
            print("go ahead...")
            voicee = listener.listen(source)
            request = listener.recognize_google(voicee)
            print(request)
            sayit(request)
            audio.say(request)
            
    except:
        pass
'''

class ScreenManager(ScreenManager):
    pass

class MyAppApp(App):
    pass


MyAppApp().run()