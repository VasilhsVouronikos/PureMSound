import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

class CustomSliderGain(Slider):
	pass

class CustomSliderDrive(Slider):
	pass

class Display(App):
	def build(self):
		Config.set('graphics', 'resizable', False)
		#s = Slider(min=-100, max=100, value=25,orientation='vertical')
		return FloatLayout()



if __name__ == '__main__':
	Display().run()