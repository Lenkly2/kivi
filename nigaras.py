from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

class Timer(App):
    

    def build(self):
        self.total_second = 0
        self.running = False
        self.button_start = Button(text="Start",on_press=self.start)
        self.button_stop = Button(text="Stop",on_press=self.stop)
        self.button_reset = Button(text="Reset",on_press=self.reset)

        self.text = Label(text="00:00:00")
        self.layout = BoxLayout(orientation="vertical")
        self.layout.add_widget(self.button_start)
        self.layout.add_widget(self.button_stop)
        self.layout.add_widget(self.button_reset)
        self.layout.add_widget(self.text)
        return self.layout                
          
    def update_timer(self,instance):
        self.total_second +=1
        hour, ostacha = divmod(self.total_second,3600)
        minute, second = divmod(ostacha,60)
        self.text.text = f"{hour:02}:{minute:02}:{second:02}"
    def start(self,instance):
        if self.running == False:
            self.running = True
            Clock.schedule_interval(self.update_timer,1)
    def stop(self,instance):
        if self.running:
            self.running = False
            Clock.unschedule(self.update_timer)
    def reset(self,instance):
        self.stop(instance)
        self.total_second = 0
        self.text.text = "00:00:00"
app = Timer()
app.run()