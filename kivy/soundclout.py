from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button,Label
from kivy.graphics import Color,Rectangle,InstructionGroup

class DeviceTemplateScreen(Screen):
	pass

class GroupTemplateScreen(Screen):
	
	def remove(self):
		pass

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
	
	scan_list = ['Pi-1','Pi-2','Pi-3','Pi-4','Pi-5']
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
	#Groups = [GroupNo,null]
	Groups = [[1,10],[2,20]]

	def on_enter(self):

		for i in xrange(0,len(EditDeviceGroupsScreen().Groups)):
			print(str(EditDeviceGroupsScreen().Groups[i][0]))

		print('HERE')

		self.ids.glayout2.clear_widgets()
		for i in xrange(0,len(EditDeviceGroupsScreen().Groups)):
			addedGroup = BoxLayout(size_hint_y=None,height='120sp',orientation='horizontal')
			addedButton=Button(text="Group " + str(EditDeviceGroupsScreen().Groups[i][0]) + " Settings",font_size=25)
			addedButton.bind(on_press=lambda x:self.group_modification((EditDeviceGroupsScreen().Groups[i][0]+1),self.currentSlot))
			addedButton.bind(on_release=lambda x:self.nav_to_group())
			addedGroup.add_widget(addedButton)
			self.ids.glayout2.add_widget(addedGroup)


	#Removes all widget on leaving to prevent the creation of duplicate widgets
	def nav_to_group(self):
		self.manager.current = 'edit_group_behaviour_screen_9'

	def create_group(self):
		base = 1
		for i in xrange(0,len(EditDeviceGroupsScreen().Groups)):
			if base < EditDeviceGroupsScreen().Groups[i][0]:
				base = EditDeviceGroupsScreen().Groups[i][0]
		EditDeviceGroupsScreen().Groups.append([base+1,(base+1)*10])		

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

	def currentSlot():
		pass

class SelectGroupScreen(Screen):
	#reassignment in EditTimelineScreen.glayout
	currentSlot = 0

	#Adds all the widgets from the group list
	def on_enter(self):
		self.ids.glayout2.clear_widgets()
		for i in xrange(0,len(EditDeviceGroupsScreen().Groups)):
			addedGroup = BoxLayout(size_hint_y=None,height='120sp',orientation='horizontal')
			addedButton=Button(text="Group " + str(EditDeviceGroupsScreen().Groups[i][0]) + " Settings",font_size=25)
			addedButton.bind(on_press=lambda x:self.group_modification((EditDeviceGroupsScreen().Groups[i][0]+1),self.currentSlot))
			addedButton.bind(on_release=lambda x:self.nav_to_group())
			addedGroup.add_widget(addedButton)
			self.ids.glayout2.add_widget(addedGroup)

	#Removes all widget on leaving to prevent the creation of duplicate widgets
	def nav_to_group(self):
		self.manager.current = 'edit_group_behaviour_screen_9'

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

	#adds the four tuple to EditGroupBehaviourScreen.groupSettings list if it isnt present. it it already exist return with no change
	def add_settings(self):
		tempSettings = []
		print('EditGroupBehaviourScreen.add_settings')
		for i in xrange(0,len(self.groupSettings)):
		 	if self.groupSettings[i][0]==self.groupNumber and self.groupSettings[i][1]==self.timelineNumber:
		 			print('exist')
		 			return			
		print('added')
		tempSettings = [self.groupNumber,self.timelineNumber,0,0]
		self.groupSettings.append(tempSettings)

	#finds and reads four tuple for timeline element to update slider position and switch position
	#for now refresh settings are disabled although save_changes works
	def refresh_settings(self):
		pass

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
	select_group_screen = ObjectProperty()
	edit_group_behaviour_screen = ObjectProperty()
	device_template_screen = ObjectProperty()
 	group_template_screen= ObjectProperty()

	def update(self):
		self.connected_device_list._trigger_reset_populate()
		self.current_screen.update()

# The device class that will hold device name, number, and port for sending information
# May also hold group number at a later date
class Device():

	def __init__(self, n="Null", num=-1, p=-1):
		self.name = n
		self.number = num
		self.port = p

	def signalDevice(self):
		pass
		# TODO handle filling this out

# A class representing the groups being saved in the app
# holds a list of devices in the group and the saved group parameters
class Group():

	#groupSettings = [groupNumber-starting at 1,timelineNumber-starting at 1,switchActive,sliderValue]
	def __init__(self, devList = [], groupParams = []):
		self.devices = devList
		self.groupSettings = groupParams

	def signalGroup(self):
		pass
		# TODO handle the event triggering


class SoundCloutApp(App):
	
	def build(self):
		return Manager(transition=WipeTransition())

if  __name__=='__main__':
	SoundCloutApp().run()