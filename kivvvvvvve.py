from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.videoplayer import VideoPlayer
import pyautogui
import random
ab = 0
class APPPX(App):
    def build(self):
        global ab
        layaut = BoxLayout(orientation = "vertical")
        layat = BoxLayout()
        label = Label(text = "history of europa")
        button = Button(text = "idi naxyi",on_press=self.plj)
        a = VideoPlayer(source='git.mp4', state='play',
        options={'fit_mode': 'contain'})
        layat.add_widget(a)
        layaut.add_widget(button)
        layaut.add_widget(label)

        layat.add_widget(layaut)
        if ab == 1:
            while True:
                x,y = random.randint(0,1900),random.randint(0,720)
                pyautogui.moveTo(x,y)
        return layat
    def plj(self,b):
        global ab
        print("b")
        



app = APPPX()
app.run()