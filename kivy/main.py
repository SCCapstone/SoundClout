from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooser
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button,Label
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.graphics import Color,Rectangle,InstructionGroup
from kivy.uix.rst import RstDocument
from timelinereader import timelineReader
import io
import os, errno



class HomeScreen(Screen):
	skipBuild = 'build_timeline_screen_6'

	#skips build option if already timeline is already built
	def skip_build_screen(self,value):
		if value is 1:
			self.skipBuild = 'edit_timeline_screen_7'

class RunScreen(Screen):
	pass

class DeviceTesterScreen(Screen):

	def refresh_devices_list(self):
		#refresh devices list
		self.connected_device_list._trigger_reset_populate()

class ConnectDevicesScreen(Screen):

	scan_list = ['Pi-1','Pi-2','Pi-3','Pi-4','Pi-5']
	applied_list =[]

	def connect_device(self):
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

			for i in xrange(0,len(ConnectDevicesScreen.scan_list)):
				if ConnectDevicesScreen.scan_list[i]==selection:
					ConnectDevicesScreen.applied_list.append(selection)
					del ConnectDevicesScreen.scan_list[i]
					return

	def disconnect_device(self):
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

			for i in xrange(0,len(ConnectDevicesScreen.applied_list)):
				if ConnectDevicesScreen.applied_list[i]==selection:
					ConnectDevicesScreen.scan_list.append(selection)
					del ConnectDevicesScreen.applied_list[i]
					return


	def on_leave(self):
		print (self.scan_list)
		print (self.applied_list)

class DeviceListButton(ListItemButton):
	pass

class EditDeviceGroupsScreen(Screen):
	#Groups = [GroupNo,null]
	Groups = []
	loaded_config = []


	def on_enter(self):
		self.ids.glayout2.clear_widgets()
		for i in xrange(0,len(self.manager.groupList)):
			addedGroup = BoxLayout(size_hint_y=None,height='120sp',orientation='horizontal')
			addedButton=Button(text="Group " + self.manager.groupList[i].name + "\'s Settings",
							   font_size=25,
							   id=self.manager.groupList[i].name,
							   on_release=self.press_btn
							   )
			addedGroup.add_widget(addedButton)
			self.ids.glayout2.add_widget(addedGroup)

	#on press, send group id to group template and transition to template screen
	def press_btn(self,instance):
		GroupTemplateScreen.currentGroupNo=instance.text[6]
		self.manager.current = 'group_template_screen_11'

	def create_group(self):
		group = Group(self.manager.create_group_screen.ids.group_name.text, devList = [], groupParams = [])
		self.manager.groupList.append(group)

## Save/Load
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_save(self):
		content = SaveDialogScreen(save=self.save, cancel=self.dismiss_popup)
		self._popup = Popup(title="Save File", content=content, size_hint=(0.9,0.9))
		self._popup.open()

	def save(self, path, filename):
		with open(os.path.join(path, filename), 'w') as stream:
			stream.write(self.RecordConfiguration())
		self.dismiss_popup()

	def show_load(self):
		content = LoadDialogScreen(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Load file", content=content,
							size_hint=(0.9, 0.9))
		self._popup.open()

	def load(self, path, filename):
		with open(os.path.join(path, filename[0])) as stream:
			self.loaded_config = stream.read().splitlines()
			self.LoadConfiguration()
			self.on_enter()
		self.dismiss_popup()
	#concatenates all groups in ScreenManager.groupList onto a string
	def RecordConfiguration(self):
		s = ""
		for i in range(len(self.manager.groupList)):
			s = s + self.manager.groupList[i].name
			s = s + '\n'
			for j in range(len(self.manager.groupList[i].devList)):
				s = s + self.manager.groupList[i].devList[j].n + ', '
				s = s + self.manager.groupList[i].devList[j].num + ', '
				s = s + self.manager.groupList[i].devList[j].p + ', '
			s = s + '\n'
			for j in range(len(self.manager.groupList[i].groupSettings)):
				s = s + self.manager.groupList[i].groupSettings[j] + ', '
			s = s + '\n'
		return s

	def LoadConfiguration(self):
		self.manager.groupList = []
		for i in range(0, len(self.loaded_config), 3):
			if not self.loaded_config[i]:
				break
			group = Group(self.loaded_config[i],[],[])
			self.manager.groupList.append(group)
			pass


# could be fused with EditDeviceGroupsScreen
class CreateGroupScreen(Screen):
	pass

class BuildTimelineScreen(Screen):
	pass

class EditTimelineScreen(Screen):
	skipBuild = 'build_timeline_screen_6'

	#skips build option if already timeline is already built
	def skip_build_screen(self,value):
		if value is 1:
			self.skipBuild = 'edit_timeline_screen_7'

	def currentSlot():
		pass

class SelectGroupScreen(Screen):
	#reassignment in EditTimelineScreen.glayout
	currentSlot = 0

	#Adds all the widgets from the group list
	def on_enter(self):
		self.ids.glayout2.clear_widgets()
		for i in xrange(0,len(self.manager.groupList)):
			addedGroup = BoxLayout(size_hint_y=None,height='120sp',orientation='horizontal')
			addedButton=Button(text="Group " + self.manager.groupList[i].name + " Settings",font_size=25)
			addedButton.bind(on_press=lambda x:self.group_modification(i,self.currentSlot))
			addedButton.bind(on_release=lambda x:self.nav_to_group())

			addedGroup.add_widget(addedButton)
			self.ids.glayout2.add_widget(addedGroup)

	def nav_to_group(self):
		self.manager.current = 'edit_group_behaviour_screen_9'

	#triggers on press of any timeline button assigning group number and timeline number to GroupBehaviourScreen.groupNumber and GroupBehaviourScreen.timelineNumber
	def group_modification(self,groupNumber,timelineNumber):
		#assign group and device number so modifications can be made
		EditGroupBehaviourScreen.groupNumber=groupNumber
		EditGroupBehaviourScreen.timelineNumber=timelineNumber
		#adds the four tuple to EditGroupBehaviourScreen.groupSettings list if it isnt present, otherwise, loads current switch position and slider amount
		EditGroupBehaviourScreen().add_settings()

class DeviceTemplateScreen(Screen):
	pass

class GroupTemplateScreen(Screen):
	currentGroupNo=0
	connectedDevices=[]


	def on_enter(self):
		#Clear all labels
		self.ids.groupName.clear_widgets()
		self.ids.devicesConnected.clear_widgets()


		#Add back labels for the group and devices connected
		self.ids.groupName.add_widget(Label(text="Name:",font_size=35))
		#self.ids.groupName.add_widget(Label(text="Group " + str(self.currentGroupNo),font_size=35))
		#NEEDS TO BE CHANGED TO DISPLAY ACTUAL GROUP DATA
		self.ids.groupName.add_widget(Label(text=self.manager.create_group_screen.ids.group_name.text,font_size=35))

		self.ids.devicesConnected.add_widget(Label(text="Status:",font_size=35))
		self.ids.devicesConnected.add_widget(Label(text=str(' Inactive'),font_size=35))

		self.ids.devicelisting.clear_widgets()
		for i in xrange(0,len(ConnectDevicesScreen().applied_list)):
			addedGroup = BoxLayout(size_hint_y=None,height='75sp',orientation='horizontal')

			addedGroup.add_widget(Label(text="Device " + ConnectDevicesScreen().applied_list[i],font_size=25,color=(0,0,0,1)))

			switch=Switch(active=False,id=ConnectDevicesScreen().applied_list[i])
			switch.bind(active=self.switch_on)
			addedGroup.add_widget(switch)

			self.ids.devicelisting.add_widget(addedGroup)

	def removeGroup(self):
		del EditDeviceGroupsScreen.Groups[int(self.currentGroupNo)-1]

	#saving this for when Group names have to be deleted by name matching
	def removeGroupMatching(self):
		for i in range(0, len(EditDeviceGroupsScreen().Groups)):
			if self.currentGroupNo == EditDeviceGroupsScreen().Groups[i][0]:
				del (EditDeviceGroupsScreen.Groups[i])

	def switch_on(self,instance, value):
		print (instance)
		print (value)

#		if value is active:
#			rint("Checkbox Checked")
#		else:
#			rint("Checkbox Unchecked")


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
		for i in xrange(0,len(self.groupSettings)):
		 	if self.groupSettings[i][0]==self.groupNumber and self.groupSettings[i][1]==self.timelineNumber:
		 			return
		tempSettings = [self.groupNumber,self.timelineNumber,0,0]
		self.groupSettings.append(tempSettings)

	#finds and reads four tuple for timeline element to update slider position and switch position
	#for now refresh settings are disabled although save_changes works
	def refresh_settings(self):
		pass

	def reset_settings(self):
		self.groupSettings = []

	#if save changes button is pressed, update four tuple on group timeline

	def save_changes(self,timelineNumber,switchActive,sliderValue):
		#find element
		for i in xrange(0,len(self.groupSettings)):
		 	if self.groupSettings[i][0]==self.groupNumber and self.groupSettings[i][1]==self.timelineNumber:
		 			#update element
					self.groupSettings[i][1] = timelineNumber
					self.groupSettings[i][2] = switchActive
					self.groupSettings[i][3] = sliderValue
					print(self.groupSettings)
					j = timelineReader(self.groupSettings[i],1,2,str(self.groupSettings[i][0]))
					j.MonthGroupBehavior()

	#need to finish logic to detect position of switch and feed to four tuple. for now assume switch is active all the time
	def switch_on(self, value):
		if value is True:
			print("Switch On")
		else:
			print("Switch Off")
	def back_out(self):
		pass

class SaveDialogScreen(Screen):

	save = ObjectProperty(None)
 	cancel = ObjectProperty(None)

	wd = os.getcwd()

class LoadDialogScreen(Screen):

	load = ObjectProperty(None)
	cancel = ObjectProperty(None)
	wd = os.getcwd()




#manages screens
class Manager(ScreenManager):
	#list of current groups
	groupList = []

	home_screen = ObjectProperty()
	run_screen = ObjectProperty()
	device_tester_screen = ObjectProperty()
	connect_devices_screen = ObjectProperty()
	edit_device_groups_screen = ObjectProperty()
	create_group_screen = ObjectProperty()
	save_dialog_screen = ObjectProperty()
	load_dialog_screen = ObjectProperty()
	build_timeline_screen = ObjectProperty()
	edit_timeline_screen = ObjectProperty()
	select_group_screen = ObjectProperty()
	edit_group_behaviour_screen = ObjectProperty()
	device_template_screen = ObjectProperty()
	group_template_screen = ObjectProperty()
	add_remove_device_selection_screen = ObjectProperty()
	add_remove_device_info_screen = ObjectProperty()

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
	def __init__(self,name, devList = [], groupParams = []):
		self.name = name
		self.devList = devList
		self.groupSettings = groupParams

	def signalGroup(self):
		pass
		# TODO handle the event triggering

class SoundCloutApp(App):
	def build(self):
		return Manager(transition=WipeTransition())

if  __name__=='__main__':

	SoundCloutApp().run()
