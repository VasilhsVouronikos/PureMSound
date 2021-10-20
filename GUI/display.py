import kivy
from kivy.config import Config
Config.set('graphics', 'resizable', False)


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionItem
from kivy.uix.actionbar import ActionButton
from kivy.uix.actionbar import ActionBarException
import os,sys
import threading




def get_current_path():
	path = os.getcwd().split("\\")
	path.pop(0)
	path.pop(len(path)-1)
	path.append("FX")
	path.append("DirtyDrive")
	new_path = "\\"+"\\".join(path)
	
	return new_path

path_to_FX = get_current_path()
sys.path.insert(0,path_to_FX)

from Ddrive import update,init,change_drive,reset_to_original

class CustomSliderGain(Slider):
	pass

class CustomSliderDrive(Slider):
	pass

class Display(App):
	def build(self):
		self.p = None
		self.wf = None
		self.stream = None
		self.CHUNK = None
		self.wav = None
		#s = Slider(min=-100, max=100, value=25,orientation='vertical')
		p,wf,stream,CHUNK,wav = init()

		self.p = p
		self.wf = wf
		self.stream = stream
		self.CHUNK = CHUNK

		threading.Thread(target = self.update_au, args=([250])).start()

		return FloatLayout()
	def update_au(self,val):
		update(self.p,self.wf,self.stream,self.CHUNK)

		return
	def init_au(self):
		p,wf,stream,CHUNK,wav = init()
		return p,wf,stream,CHUNK,wav

	def send_val(self,val):
		change_drive(val)


if __name__ == '__main__':
	Display().run()