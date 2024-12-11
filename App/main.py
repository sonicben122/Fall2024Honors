from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests
import webbrowser
from kivy.core.window import Window


#steam api
base_url = "http://api.steampowered.com"

def get_cs2_news():
    url = f"{base_url}/ISteamNews/GetNewsForApp/v0002/?appid=730&count=4&maxlength=300&format=json"
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
    update4 = newsitems[3]

    #title
    latestupdatetitle = latestupdate["title"]
    update2title = update2["title"]
    update3title = update3["title"]
    update4title = update4["title"]
    #url
    latestupdateurl = latestupdate["url"]
    update2url = update2["url"]
    update3url = update3["url"]
    update4url = update4["url"]


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
    def callback4(instance):
        print('The button3 <%s> is being pressed' % instance.text)
        webbrowser.open(update4url)




class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if cs2_info:
            #definds buttons and lables
            l1 = Label(text="Counter Strike News", size_hint=("1", ".5"), color="black")
            b1 = Button(text="Latest Update: " + str(latestupdatetitle))
            b2 = Button(text="Second Update: " + str(update2title))
            b3 = Button(text="Third Update: " + str(update3title))
            b4 = Button(text="Forth Update: " + str(update4title))
            #adds them to widget
            self.add_widget(l1)
            self.add_widget(b1)
            self.add_widget(b2)
            self.add_widget(b3)
            self.add_widget(b4)

            #binds buttons to callback
            b1.bind(on_press=callback)
            b2.bind(on_press=callback2)
            b3.bind(on_press=callback3)
            b4.bind(on_press=callback4)
        else:
            le = Label(text="Can't reach site")
            self.add_widget(le)

class MainWidget(Widget):
    pass


class CS2UpdateApp(App):
    def build(self):
        #defins background color
        Window.clearcolor = (1, .647, 0)
        return super().build()

if __name__ == "__main__":
    CS2UpdateApp().run()