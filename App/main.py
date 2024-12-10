from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests
import urllib.request

#steam api
base_url = "http://api.steampowered.com"

def get_cs2_news():
    url = f"{base_url}/ISteamNews/GetNewsForApp/v0002/?appid=730&count=3&maxlength=300&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to get data {response.status_code}")


cs2_info = get_cs2_news()

if cs2_info:
    appnews = cs2_info["appnews"]
    newsitems = appnews["newsitems"]
    latestupdate = newsitems[0]
    update2 = newsitems[1]
    update3 = newsitems[2]

    latestupdatetitle = latestupdate["title"]
    update2title = update2["title"]
    update3title = update3["title"]

def callback(instance):
    print('The button <%s> is being pressed' % instance.text)
    if instance == :
        
    

    # urllib.request.urlopen('https://www.javatpoint.com/python-tutorial')  



class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        l1 = Label(text="CS2 Updates", size_hint=(1, .5))
        b1 = Button(text=str(latestupdatetitle))
        b2 = Button(text=str(update2title))
        b3 = Button(text=str(update3title))
        self.add_widget(l1)
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        b1.bind(on_press=callback)
        b2.bind(on_press=callback)

class MainWidget(Widget):
    pass


class CS2UpdateApp(App):
    pass


CS2UpdateApp().run()