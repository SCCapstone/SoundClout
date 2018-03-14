from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
	skipBuild = 'build_timeline_screen_6'

	#skips build option if already being built
	def skip_build_screen(self,value):
		if value is 1:
			print("skip_build_screen")
			HomeScreen.skipBuild = 'edit_timeline_screen_7'

class RunScreen(Screen):
	pass

class DeviceTesterScreen(Screen):
	pass

class ConnectDevicesScreen(Screen):
	pass

class EditDeviceGroupsScreen(Screen):
	pass

class BuildTimelineScreen(Screen):
	pass

class EditTimelineScreen(Screen):
	pass

class EditGroupBehaviourScreen(Screen):
	pass


		

class Manager(ScreenManager):

	home_screen = ObjectProperty()
	run_screen = ObjectProperty()
	device_tester_screen = ObjectProperty()
	connect_devices_screen = ObjectProperty()
	edit_device_groups_screen = ObjectProperty()
	build_timeline_screen = ObjectProperty()
	edit_timeline_screen = ObjectProperty()
	edit_group_behaviour_screen = ObjectProperty()

class SoundCloutApp(App):
	
	def build(self):
		return Manager(transition=WipeTransition())

if  __name__=="__main__":
	SoundCloutApp().run()
