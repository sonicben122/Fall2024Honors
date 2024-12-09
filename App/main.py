from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests

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


class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text=str(latestupdatetitle))
        self.add_widget(b1)

class MainWidget(Widget):
    pass


class ClassView(App):
    pass


ClassView().run()