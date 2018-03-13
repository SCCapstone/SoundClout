from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
	pass

class RunScreen(Screen):
	pass

class DeviceTesterScreen(Screen):
	pass

class ConnectDevicesScreen(Screen):
	pass

class EditDeviceGroupsScreen(Screen):
	pass

class EditGroupBehaviourScreen(Screen):
	pass

class Manager(ScreenManager):

	home_screen = ObjectProperty()
	run_screen = ObjectProperty()

	connect_devices_screen = ObjectProperty()

class SoundCloutApp(App):
	
	def build(self):
		return Manager(transition=WipeTransition())

if  __name__=="__main__":
	SoundCloutApp().run()
