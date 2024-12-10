from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests
import webbrowser


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

    #title
    latestupdatetitle = latestupdate["title"]
    update2title = update2["title"]
    update3title = update3["title"]
    #url
    latestupdateurl = latestupdate["url"]
    update2url = update2["url"]
    update3url = update3["url"]


    #Def what button dose
    def callback(instance):
        print('The button1 <%s> is being pressed' % instance.text)
        webbrowser.open(latestupdateurl)
    def callback2(instance):
        print('The button2 <%s> is being pressed' % instance.text)
        webbrowser.open(update2url)
    def callback3(instance):
        print('The button3 <%s> is being pressed' % instance.text)
        webbrowser.open(update3url)




class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if cs2_info:
            b1 = Button(text=str(latestupdatetitle))
            b2 = Button(text=str(update2title))
            b3 = Button(text=str(update3title))
            self.add_widget(b1)
            self.add_widget(b2)
            self.add_widget(b3)
            b1.bind(on_press=callback)
            b2.bind(on_press=callback2)
            b3.bind(on_press=callback3)
        else:
            le = Label(text="Can't reach site")
            self.add_widget(le)

class MainWidget(Widget):
    pass


class CS2UpdateApp(App):
    pass

if __name__ == "__main__":
    CS2UpdateApp().run()