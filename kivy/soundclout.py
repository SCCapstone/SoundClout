from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
	skipBuild = 'build_timeline_screen_6'

	#skips build option if already timeline is already built
	def skip_build_screen(self,value):
		if value is 1:
			print('HomeScreen.skip_build_screen')
			self.skipBuild = 'edit_timeline_screen_7'

class RunScreen(Screen):
	pass

class DeviceTesterScreen(Screen):

	def refresh_devices_list(self):
		print('DeviceTesterScreen.refresh_devices_list')
		#refresh devices list
		self.connected_device_list._trigger_reset_populate()


class ConnectDevicesScreen(Screen):

	scan_list = ['Pi-1','Pi-2','Pi-3']
	applied_list =['']

	def connect_device(self):
		print('ConnectDevicesScreen.connect_device')
		#if device is selected
		if self.device_list.adapter.selection:
			#get selection
			selection = self.device_list.adapter.selection[0].text
			#remove from available devices
			self.device_list.adapter.data.remove(selection)
			#add to connected devices
			self.connected_device_list.adapter.data.extend([selection])
			#refresh both device list and connected devices list
			self.device_list._trigger_reset_populate()
			self.connected_device_list._trigger_reset_populate()

	def disconnect_device(self):
		print('ConnectDevicesScreen.disconnect_device')
		#if device is selected
		if self.connected_device_list.adapter.selection:
			#get selection
			selection = self.connected_device_list.adapter.selection[0].text
			#remove from available devices
			self.connected_device_list.adapter.data.remove(selection)
			#add to connected devices
			self.device_list.adapter.data.extend([selection])
			#refresh both device list and connected devices list
			self.device_list._trigger_reset_populate()
			self.connected_device_list._trigger_reset_populate()


class DeviceListButton(ListItemButton):
    pass

class EditDeviceGroupsScreen(Screen):
	pass

class BuildTimelineScreen(Screen):
	pass

class EditTimelineScreen(Screen):
	skipBuild = 'build_timeline_screen_6'

	#skips build option if already timeline is already built
	def skip_build_screen(self,value):
		print('EditTimelineScreen.skip_build_screen')
		if value is 1:
			print('skip_build_screen')
			self.skipBuild = 'edit_timeline_screen_7'

	#triggers on press of any timeline button assigning group number and timeline number to GroupBehaviourScreen.groupNumber and GroupBehaviourScreen.timelineNumber
	def group_modification(self,groupNumber,timelineNumber):
		print('EditGroupBehaviourScreen('+str(groupNumber)+','+str(timelineNumber)+')')
		#assign group and device number so modifications can be made
		EditGroupBehaviourScreen.groupNumber=groupNumber
		EditGroupBehaviourScreen.timelineNumber=timelineNumber
		#adds the four tuple to EditGroupBehaviourScreen.groupSettings list if it isnt present, otherwise, loads current switch position and slider amount
		EditGroupBehaviourScreen().add_settings()

class EditGroupBehaviourScreen(Screen):
	groupNumber = 0
	timelineNumber = 0
	switchActive = 0
	sliderValue = 0

	#groupSettings = [groupNumber-starting at 1,timelineNumber-starting at 1,switchActive,sliderValue]
	groupSettings = []
	def print_out(self):
		print self.groupNumber
		print self.timelineNumber

	#adds the four tuple to EditGroupBehaviourScreen.groupSettings list if it isnt present. it it already exist return with no change
	def add_settings(self):
		tempSettings = []
		print('EditGroupBehaviourScreen.add_settings')
		for i in xrange(0,len(self.groupSettings)):
		 	if self.groupSettings[i][0]==self.groupNumber and self.groupSettings[i][1]==self.timelineNumber:
		 			print('exist')
		 			return
		print('added')
		#EditGroupBehaviourScreen().back_out()
		tempSettings = [self.groupNumber,self.timelineNumber,0,0]
		self.groupSettings.append(tempSettings)

	#finds and reads four tuple for timeline element to update slider position and switch position
	#for now refresh settings are disabled although save_changes works
	def refresh_settings(self):
		pass

	#if settings aren't changed, back out and dont change settings(currently using it to print four tuple)
	def back_out(self):
		print('EditGroupBehaviourScreen.back_out')
		for i in xrange(0,len(self.groupSettings)):
			# if groupSettings[i][0]==groupNumber:
			# 	if groupSettings[i][1]==timelineNumber:
			# 		continue
			print self.groupSettings[i][0]
			print self.groupSettings[i][1]
			print self.groupSettings[i][2]
		 	print self.groupSettings[i][3]

	def reset_settings(self):
		self.groupSettings = []

	#if save changes button is pressed, update four tuple on group timeline
	def save_changes(self,switchActive,sliderValue):
		#find element
		for i in xrange(0,len(self.groupSettings)):
		 	if self.groupSettings[i][0]==self.groupNumber and self.groupSettings[i][1]==self.timelineNumber:
		 			print('found')
		 			#update element
		 			self.groupSettings[i][2] = switchActive
		 			self.groupSettings[i][3] = sliderValue

	#need to finish logic to detect position of switch and feed to four tuple. for now assume switch is active all the time
	def switch_on(self, value):
		if value is True:
			print("Switch On")
		else:
			print("Switch Off")

#manages screens
class Manager(ScreenManager):

	home_screen = ObjectProperty()
	run_screen = ObjectProperty()
	device_tester_screen = ObjectProperty()
	connect_devices_screen = ObjectProperty()
	edit_device_groups_screen = ObjectProperty()
	build_timeline_screen = ObjectProperty()
	edit_timeline_screen = ObjectProperty()
	edit_group_behaviour_screen = ObjectProperty()

	def update(self):
		self.connected_device_list._trigger_reset_populate()
		self.current_screen.update()

class SoundCloutApp(App):

	def build(self):
		return Manager(transition=WipeTransition())

if  __name__=='__main__':
	SoundCloutApp().run()
