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
        label = Label(text="main window")
        layaut.add_widget(label)
        button = Temate_button(self,direction="down",goal="nw",text="Borderlands")
        layaut.add_widget(button)
        self.add_widget(layaut)

class new_fil_Borderlands(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layaut = BoxLayout(orientation = "vertical")
        button = Temate_button(self,direction="up",goal="main",text="main")
        a = VideoPlayer(source='borde.mp4', state='pause',
        options={'fit_mode': 'contain'})
        layaut.add_widget(a)
        label = Label(text_size =(600,None),text="Про фільм за мотивами однойменної серії відеоігор від Gearbox Software ми вже писали у Топі майбутніх екранізацій забавок. Елай Рот займався режисурою, потім було двотижневе перефільмування, на якому його замінив Тім Міллер. Влітку стало відомо, що Крейг Мазін не є автором чи співавтором сценарію, як зазначалося раніше. Зрештою, якийсь час проєкт знаходився у поствиробничому пеклі, що напевно позначиться на якості продукту, але, здається, студія Lionsgate нарешті готова випустити його на екрани.За сюжетом сумнозвісна злочинниця із загадковим минулим Ліліт (Кейт Бланшетт) неохоче повертається на свою рідну планету Пандору і укладає несподівану угоду. Вона береться знайти зниклу доньку Атласа, об’єднавши зусилля з іншими персонажами гри. Усі вони вирушають у сповнену небезпек пригоду.")
        layaut.add_widget(label)
        layaut.add_widget(button)
        self.add_widget(layaut)
class myapp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(main_Cod(name="main"))
        manager.add_widget(new_fil_Borderlands(name="nw"))
        return manager
    
app = myapp()
app.run()