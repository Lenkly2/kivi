from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer

class Temate_button(Button):
    def __init__(self,screen,direction="right",goal="main" ,**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class main_Cod(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layaut = BoxLayout(orientation = "vertical")
        a = VideoPlayer(source='git.mp4', state='play',
        options={'fit_mode': 'contain'})
        layaut.add_widget(a)
        button = Temate_button(self,direction="down",goal="nw",text="dd")
        layaut.add_widget(button)
        self.add_widget(layaut)

class new_window(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layaut = BoxLayout(orientation = "vertical")
        button = Temate_button(self,direction="up",goal="main",text="dd")
        label = Label(text="nigger")
        layaut.add_widget(label)
        layaut.add_widget(button)
        self.add_widget(layaut)
class myapp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(main_Cod(name="main"))
        manager.add_widget(new_window(name="nw"))
        return manager
    
app = myapp()
app.run()