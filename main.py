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
import openai





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

class ConvertorScreen(Screen):

    def convert(self):
     
     from_ = self.ids.fromss.text.upper()

     to_ = self.ids.tooo.text.upper()

     resultt = self.ids.res

     amount = self.ids.amounts.text
     convert = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_}&to={to_}")
     resultt.text = f"{convert.json()['rates'][to_] }  {to_}"
     print(f"{amount}  {from_} is {convert.json()['rates'][to_]}  {to_}")

class AirwaysScreen(Screen): #DONE
    pass

class LocationsScreen(Screen):
    pass

class EducatScreen(Screen):#DONE
    pass

class BritishAirwaysScreen(Screen):#DONE
    pass
    #def show(self):
       # datePicker = MDDatePicker(year=2023,month=9,day=13)
        #datePicker.open()

class UniUkScreen(Screen): 
    pass

class OxfordScreen(Screen):#done
    oxftext = '''The University of Oxford is a collegiate research university in Oxford, England.There is evidence of teaching as early as 1096,making it the oldest university in the English-speaking world and the world's second-oldest university in continuous operation.It grew rapidly from 1167 when Henry II banned English students from attending the University of Paris.After disputes between students and Oxford townsfolk in 1209, some academics fled north-east to Cambridge where they established what became the University of Cambridge.The two English ancient universities share many common features and are jointly referred to as Oxbridge. The university is made up of thirty-nine semi-autonomous constituent colleges, four permanent private halls, and a range of academic departments which are organised into four divisions.All the colleges are self-governing institutions within the university, each controlling its own membership and with its own internal structure and activities. All students are members of a college. It does not have a main campus, and its buildings and facilities are scattered throughout the city centre. Undergraduate teaching at Oxford consists of lectures, small-group tutorials at the colleges and halls, seminars, laboratory work and occasionally further tutorials provided by the central university faculties and departments. Postgraduate teaching is provided in a predominantly centralized fashion. Oxford operates the Ashmolean Museum, the world's oldest university museum; Oxford University Press, the largest university press in the world; and the largest academic library system nationwide.In the fiscal year ending 31 July 2022, the university had a total consolidated income of £2.78 billion, of which £711.4 million was from research grants and contracts. Oxford has educated a wide range of notable alumni, including 30 prime ministers of the United Kingdom and many heads of state and government around the world.As of October 2022, 73 Nobel Prize laureates, 4 Fields Medalists, and 6 Turing Award winners have matriculated, worked, or held visiting fellowships at the University of Oxford, while its alumni have won 160 Olympic medals. Oxford is the home of numerous scholarships, including the Rhodes Scholarship, one of the oldest international graduate scholarship programmes.'''
    

class HotelsScreen(Screen):#DONE
    pass

class AvaitorHotelScreen(Screen):
    avatext = '''Aviator is an independent hotel for elite travellers moving between London and the world's leading destinations.

Located near London in Farnborough, Hampshire, Aviator opened in 2008 as one of the most striking design hotels in recent times. Innately stylish, Aviator binds the timeless glamour of aviation with seductive interiors and ultimate comfort.

The bedroom interiors are contemporary yet rich and comfortable with walnut panelling, leather accented furniture and bathrooms with black glass walls, granite vanity tops and chrome finishing. Sky Suites amplify the indulgent personality of the hotel with walk in wardrobes, generous bath tubs, Missoni blankets and space to lounge surrounded by dark wood Venetian blinds. Guests can discreetly access the fitness studio from their rooms using a guest only stairwell at the north end of the building.

The lobby and atrium of the hotel present One Eleven, the Brasserie and Sky Bar which overlooks the private Farnborough airport.

Within the Brasserie sit two of the hotel's private dining rooms, exemplifying the intimacy and allure of the dining experience. The variety of fresh and classical dishes are accompanied by carefully selected boutique wines from producers around the world.

Located on the first floor is Sky Bar, a cocktail bar designed with intention. Secluded black leather Rocket chairs and relaxing lounge areas create the ultimate place to sip our signature cocktails.

The design of event spaces at Aviator are well considered. The private entrance to the events wing and dedicated relaxing lounge areas provide direct access to the versatile meeting rooms. Used exclusively for tailored events and celebrations, the Sky Lounge overlooks awesome views of the airport and combines with the atrium to create a venue that promises to leave a lasting impression.'''


class DakotaHotelScreen(Screen):
    dakotatext= '''Dakota Hotels is a UK-based hotel brand with five locations, each with a brasserie-style Grill and cocktail Bars. Dakota Hotels first opened two boutique hotels near Edinburgh Airport in South Queensferry, and in Eurocentral, Motherwell South East of Glasgow. The brand has now expanded into Central Glasgow, Leeds, and Manchester. The brand was founded by Ken McCulloch and is owned by Evans Property Group.
    The brand was named after the Douglas DC-3 aircraft introduced in 1936 for commercial air travel in the United States, which was designated the Dakota in Royal Air Force service.
The press have reported celebrities as staying at Dakota Hotels including Hugh Jackman, Arnold Schwarzenegger, Katy Perry, Liam Gallagher, Stereophonics, The Stone Roses, Glenn Close, Melanie Brown, Noel Gallagher, Christian Slater, Gary Lineker, and Andy Murray.'''

class LondonHotelScreen(Screen):
    lontext = '''Royal Lancaster London is Hyde Park’s commanding mid-century architectural icon born and built in the swinging 60s. Our happy history has seen us hip, handsome and rolling with the times in our unrivalled London location. Today, here in the 21st century we’re proud of the knowledge and expertise we’ve gained over half a century as one of London’s leading hotels.

We enjoy the liberty of being independent and the opportunity it gives us to express our unique and genuine personality. We take pride in having a conscientious, highly professional and happy team dedicated to delivering outstanding service and ensuring that every guest experience is delightfully memorable. Whether it’s the bees in the hives on our roof, the busy staff in our corridors and kitchens, or every guest that we welcome, ‘we always care’.'''


class TransportationScreen(Screen):
    pass

class CarsScreen(Screen):
    pass


openai.api_key = "sk"

audioo = pyttsx3.init()

def audioTotext(name):
    listener = sp.Recognizer()

    with sp.AudioFile(name) as source:
        audio = listener.record(source)
    try:
        return listener.recognize_google(audio)
    except:
        print("unknown error")

def answer(question):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt=question,
        max_tokens=4000,
        n=1,
       stop=None,
       temperature=0.5    
    )
    return response['choices'][0]['text']

def speakit(text):
    audioo.say(text)
    audioo.runAndWait()

class SiriScreen(Screen):

     def main(self):
       while True:
          print("say (hello) and go ahead...")
          btn = self.ids.mic
          lab = self.ids.sayhey
          btn.source = "microphonerecord.png"
          lab.text = "say (hello) and go ahead..."
          with sp.Microphone() as source:
              listener = sp.Recognizer()
              audio = listener.listen(source)
              try:
                  script = listener.recognize_google(audio)
                  if script.lower() == 'hello':
                      name = 'input.wav'
                      print('go ahead im listening...')
                      lab.text = 'go ahead im listening...'
                      with sp.Microphone() as source:
                          listener = sp.Recognizer()
                          source.pause_threshold = 1
                          audio = listener.listen(source, phrase_time_limit=None, timeout=None)
                          with open(name, 'wb') as f:
                             f.write(audio.get_wav_data())

                      text = audioTotext(name)
                      if text:
                        print('you said:', text )

                        response = answer(text)
                        print('Hello said:', response)
                        lab.text = 'Hello said:', response

                        speakit(response)
                  elif text == 'stop':
                    break

              except Exception as e:
                 print('error: {}'.format(e))
                 lab.text = 'error: {}'.format(e)
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