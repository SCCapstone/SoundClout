# this stops the red dot issue when right clicking
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

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
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.graphics import Color,Rectangle,InstructionGroup
from kivy.uix.rst import RstDocument
from timelinereader import timelineReader
from TLR2 import TLR
import io
import copy
import os, errno
from plot import *
import sys
import bluetooth
from bluetooth import *


group = 0
class HomeScreen(Screen):
	skipBuild = 'build_timeline_screen_6'
	#skips build option if already timeline is already built
	def skip_build_screen(self,value):
		try:
			if value is 1:
				self.skipBuild = 'edit_timeline_screen_7'
		except Exception:
				print('Invalid Value in skip_build_screen!')

class RunScreen(Screen):
	def on_enter(self):
		try:
			grouplist=[]
			#TODO get cyclelength from user
			cyclelength=1
			for x in xrange(0,len(self.manager.groupList)):
				grouplist.append(self.manager.groupList[x].name)
				print("this is the number of slots "+ str(len(self.manager.edit_timeline_screen.ids.glayout3.children)))
				self.test_send(x+1)
			plot(cyclelength,len(self.manager.edit_timeline_screen.ids.glayout3.children),grouplist)


		except IndexError:
			print('No slots created!')
	def test_send(self, groupnumber):
		filename = str(groupnumber) + ".soundclout"
		sequencefile = open(filename,'r')
		testsend = sequencefile.read()
		splitup = ConnectDevicesScreen.applied_list[0].split(' ')
		addr = None
		uuid = (splitup[1])
		service_matches = find_service( uuid = uuid, address = addr)
		first_match = service_matches[0]
		port = first_match["port"]
		name = first_match["name"]
		host = first_match["host"]

		print (name)
		print (uuid)
		sock=BluetoothSocket( RFCOMM )
		sock.connect((host, port))

		data = testsend

		sock.send(data)
		sock.close()

class DeviceTesterScreen(Screen):
	deviceTestedValues = []
	def on_enter(self):

		try:
			#Clear all widgets
			self.ids.devicetestlisting.clear_widgets()
			for i in xrange(0,len(ConnectDevicesScreen.applied_list)):
				addedGroup = BoxLayout(size_hintOK_y=None,height='75sp',orientation='horizontal')

				addedGroup.add_widget(Label(text="" +ConnectDevicesScreen.applied_list[i],font_size=10,color=(0,0,0,1)))

				switch=Switch(active=True,id=ConnectDevicesScreen.applied_list[i])
				switch.bind(active=self.switch_on)
				addedGroup.add_widget(switch)

				self.ids.devicetestlisting.add_widget(addedGroup)
				self.deviceTestedValues.append(True)
		except Exception:
			print('Error in the on_enter function!')

	def switch_on(self,instance, value):
		for x in xrange(0,len(ConnectDevicesScreen.applied_list)):
			if (ConnectDevicesScreen.applied_list==instance.id):
				self.deviceTestedValues[x] = value
		print (instance.id)
		print (value)
	def testdevices(self):
		print("working")
		for x in xrange(0, len(ConnectDevicesScreen.applied_list)):
			if(self.deviceTestedValues[x]==True):
				print("testing device")
				splitup = ConnectDevicesScreen.applied_list[x].split(' ')
				addr = None
				uuid = (splitup[1])
				service_matches = find_service( uuid = uuid, address = addr)
				first_match = service_matches[0]
				port = first_match["port"]
				name = first_match["name"]
				host = first_match["host"]

				print (name)
				print (uuid)
				sock=BluetoothSocket( RFCOMM )
				sock.connect((host, port))

				data = "turn on"

				sock.send(data)
				sock.close()




class ConnectDevicesScreen(Screen):

	scan_list = []
	applied_list =[]


	def on_enter(self):
		try:
			#Clear all widgets
			self.ids.scanlisting.clear_widgets()
			self.ids.devicelisting.clear_widgets()
			for i in xrange(0,len(self.scan_list)):
				addedDevice = BoxLayout(size_hint_y=None,height='75sp',orientation='horizontal')

				addedDevice.add_widget(Button(text=self.scan_list[i],font_size=10, on_press=self.connect_device))

				self.ids.scanlisting.add_widget(addedDevice)

			for i in xrange(0,len(self.applied_list)):
				addedDevice = BoxLayout(size_hint_y=None,height='75sp',orientation='horizontal')

				addedDevice.add_widget(Button(text=self.applied_list[i],font_size=10, on_press=self.disconnect_device))

				self.ids.devicelisting.add_widget(addedDevice)
		except Exception:
			print('Error in the on_enter function!')


	#on press of scan button
	def scan(self):

		try:

			intended = None

			services = bluetooth.find_service(address=intended)
			if (len(services) == 0):
				pass
			for svc in services:
		   		testString = "" + ("Service Name: %s" % svc["name"])
		   		if "musicPi" in testString:
					testString = svc["name"] + " " + svc["service-id"]
					self.scan_list.append(testString)

		except Exception :
			print('Error scanning bluetooth')

		self.manager.current = 'loading_screen'
		self.manager.current = 'connect_devices_screen_4'




	def disconnect_all(self):
		try:

			self.applied_list = []
			self.manager.current = 'loading_screen'
			self.manager.current = 'connect_devices_screen_4'

		except Exception:
			print('Error in the disconnect_all function!')

	#connect device when pressed
	def connect_device(self,instance):
		try:
			self.applied_list.append(instance.text)
			for i in xrange(0,len(self.scan_list)):
				if self.scan_list[i] == instance.text:
					del self.scan_list[i]
			self.manager.current = 'loading_screen'
			self.manager.current = 'connect_devices_screen_4'

		except Exception:
			print('Error in the connect_device function!')

	#disconnect device when pressed
	def disconnect_device(self,instance):
		for i in xrange(0,len(self.applied_list)):
			print(self.applied_list[i])
			if self.applied_list[i] == instance.text:
				del self.applied_list[i]

		self.manager.current = 'loading_screen'
		self.manager.current = 'connect_devices_screen_4'


class DeviceListButton(ListItemButton):
	pass

class EditDeviceGroupsScreen(Screen):
	try:
		#Groups = [GroupNo,null]
		Groups = []
		loaded_config = []
		group_index = 0
	except Exception:
		print('Error in the EditDeviceGroupsScreen!')


	def on_enter(self):
		try:
			self.ids.glayout2.clear_widgets()
			for i in xrange(0,len(self.manager.groupList)):
				addedGroup = BoxLayout(size_hint_y=None,height='120sp',orientation='horizontal')
				addedButton=Button(text="Group " + str(self.manager.groupList[i].index) + ": " + self.manager.groupList[i].name + " Settings",
								   font_size=20,
								   id=self.manager.groupList[i].name,
								   on_release=self.press_btn
								   )
				addedGroup.add_widget(addedButton)
				self.ids.glayout2.add_widget(addedGroup)
		except Exception:
			print('Error in the on_enter function!')

	#on press, send group id to group template and transition to template screen
	def press_btn(self,instance):
		try:
			self.manager.group_template_screen.ids.groupNameLabel.text = instance.text[7:-9]
			#print(GroupTemplateScreen.currentGroupNo)
			self.manager.current = 'group_template_screen_11'
		except Exception:
			print('Error in the press_btn function!')

	def create_group(self):

		groupNameList = []
		for i in xrange(0, len(self.manager.groupList)):
			groupNameList.append(self.manager.groupList[i].name)

		group = Group(self.checkName(self.manager.create_group_screen.ids.group_name.text,0,groupNameList), len(self.manager.groupList)+1, devList = [], triggerList = [])
		self.manager.groupList.append(group)
		self.manager.group_template_screen.ids.groupNameLabel.text = group.name

		for i in self.manager.slotList:
			i.addGroup(group)



	def checkName(self, aName, number, nameList):

		if number is 0:
			if aName not in nameList:
				return aName
			else:
				return self.checkName(aName, (number+1), nameList)
		else:
			tempName = aName + str(number)
			if tempName not in nameList:
				return tempName
			else:
				return self.checkName(aName, number+1, nameList)

	def matchGroup(self, aGroupList,  aName):
		for i in xrange(0, len(aGroupList)):
			if aName == aGroupList[i].name:
				return aGroupList[i]



## Save/Load
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_save(self):
		try:
			content = SaveDialogScreen(save=self.save, cancel=self.dismiss_popup)
			self._popup = Popup(title="Save File", content=content, size_hint=(0.9,0.9))
			self._popup.open()
		except Exception:
			print('Error in the show_save function!')

	def save(self, path, filename):

		with open(os.path.join(path, filename), 'w') as stream:
			stream.write(self.RecordConfiguration())
		self.dismiss_popup()

		print('Error in the save function!')

	def show_load(self):
		try:
			content = LoadDialogScreen(load=self.load, cancel=self.dismiss_popup)
			self._popup = Popup(title="Load file", content=content,
								size_hint=(0.9, 0.9))
			self._popup.open()
		except Exception:
			print('Error in the show_load function!')

	def load(self, path, filename):
		try:
			with open(os.path.join(path, filename[0])) as stream:
				self.loaded_config = stream.read().splitlines()
				self.LoadConfiguration()
				self.on_enter()
			self.dismiss_popup()
		except Exception:
			print('Error in the load function!')

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
		try:
			self.manager.groupList = []
			for i in range(0, len(self.loaded_config), 3):
				if not self.loaded_config[i]:
					break
				group = Group(self.loaded_config[i],len(self.manager.groupList)+1,[],[])
				self.manager.groupList.append(group)
				pass
		except Exception:
			print('Error in the LoadConfiguration function!')

# could be fused with EditDeviceGroupsScreen
class CreateGroupScreen(Screen):
	pass

class BuildTimelineScreen(Screen):
	pass

class EditTimelineScreen(Screen):

	slots = []

	skipBuild = 'build_timeline_screen_6'

	def on_enter(self):

		pass

	#skips build option if already timeline is already built
	def skip_build_screen(self,value):
		try:
			if value is 1:
				self.skipBuild = 'edit_timeline_screen_7'
		except Exception:
			print('Error in the skip_build_screen function!')

#	def on_enter(self):
#		self.ids.glayout3.clear_widgets()
#		for i in xrange(0,len(self.slots)):
#			self.ids.glayout3.add_widget(self.slots[i])


#	def on_enter(self):
#		self.ids.glayout3.clear_widgets()
#		for i in xrange(0,len(self.slots)):
#			self.ids.glayout3.add_widget(self.slots[i])


	def currentSlot():
		pass

	def findIndexOfSlot(self, button):
		try:
			for i in range(len(self.ids.glayout3.children)):
				if button is self.ids.glayout3.children[i]:
					return i
		except Exception:
			print('Error in the findIndexOfSlot function!')

	def removeSlot(self):
		try:
			self.ids.glayout3.remove_widget(self.ids.glayout3.children[1])
		except Exception:
			print('Error in the removeSlot function!')

	def addSlot(self):

		addedButton = Button(text = "Slot " + str(len(self.ids.glayout3.children)+1), font_size = 20, size_hint_x = None, width = '200sp')
		addedButton.bind(on_press=lambda x: self.manager.select_group_screen.setSlot(self.findIndexOfSlot(addedButton)+1))
		print("Slot Number Updated")
		addedButton.bind(on_release=lambda x: self.goToSelectGroupScreen() )
		return addedButton
##################################################
	def addSlot2(self):
		slotNameList = []
		for i in xrange(0, len(self.manager.slotList)):
			slotNameList.append(self.manager.slotList[i].name)

		name = "Slot "
		addedButton = Button(text = self.checkName(name, 0, slotNameList), font_size = 20, size_hint_x = None, width = '200sp')
		#addedButton.bind(on_press=lambda x: self.manager.select_group_screen.setSlot(self.findIndexOfSlot(addedButton)+1))
		#print("Slot Number Updated 2")
		addedButton.bind(on_release=lambda x: self.goToSelectGroupScreen() )
		addedButton.bind(on_release=lambda x: self.manager.select_group_screen.setSlotName(addedButton.text))
		addedButton.bind(on_release=lambda x: self.manager.edit_group_behaviour_screen.setSlotName(addedButton.text))
		newSlot = Slot(self.checkName(name, 0, slotNameList))
		newSlot.addGroupList(copy.deepcopy(self.manager.groupList))
		self.manager.slotList.append(newSlot)
		return addedButton
###################################################

	def checkName(self, aName, number, nameList):

		if number is 0:
			if aName not in nameList:
				return aName
			else:
				return self.checkName(aName, (number+1), nameList)
		else:
			tempName = aName + '(' + str(number) + ')'
			if tempName not in nameList:
				return tempName
			else:
				return self.checkName(aName, number+1, nameList)

	def goToSelectGroupScreen(self):
		try:
			self.manager.current = 'select_group_screen_8'
		except Exception:
			print('Error in the goToSelectGroupScreen function!')

class SelectGroupScreen(Screen):
	#reassignment in EditTimelineScreen.glayout
	currentSlot = 0

	#Adds all the widgets from the group list
	def on_enter(self):
		try:
			#Refreshing Current Slot Number
			self.ids.slotnumber.clear_widgets()
			self.ids.slotnumber.add_widget(Label(size_hint_y=None,height=50))
			self.ids.slotnumber.add_widget(Label(size_hint_x=None,size_hint_y=None,height=50,width=100,text='Slot ' + str(self.currentSlot),font_size=25))

			#Refreshing Groups
			self.ids.glayout2.clear_widgets()
			#Display no groups
			if len(self.manager.groupList) == 0:
				addedGroup = BoxLayout(size_hint_y=None,height='375sp',orientation='horizontal')
				addedGroup.add_widget(Label(text="No Groups Found",font_size=25,color=(0,0,0,1)))
				self.ids.glayout2.add_widget(addedGroup)

			#Display Groups
			for i in xrange(0,len(self.manager.groupList)):
				addedGroup = BoxLayout(size_hint_y=None,height='120sp',orientation='horizontal')
				addedButton=Button(text="Group " + str(self.manager.groupList[i].index) + ": " + self.manager.groupList[i].name + " Settings",font_size=25)
				addedButton.bind(on_press=lambda x:self.group_modification(self.currentSlot))
				addedButton.bind(on_press=self.press_btn)
				addedButton.bind(on_release=lambda x:self.nav_to_group())

				addedGroup.add_widget(addedButton)
				self.ids.glayout2.add_widget(addedGroup)
			print(self.currentSlot)
		except Exception:
			print('Error in the on_enter function!')

		self.ids.glayout2.clear_widgets()
		for i in xrange(0,len(self.manager.groupList)):
			addedGroup = BoxLayout(size_hint_y=None,height='120sp',orientation='horizontal')
			addedButton=Button(text="Group " + str(i+1) +  ": " + self.manager.groupList[i].name + " Settings",font_size=25,
							   on_release=self.setGroup)


			#addedButton.bind(on_press=lambda x:self.group_modification(self.currentSlot))
			#addedButton.bind(on_release=lambda x:self.manager.edit_group_behaviour_screen.setGroupName(addedButton.text[8:-8]))
			#addedButton.bind(on_press=self.press_btn)
			addedButton.bind(on_release=lambda x:self.nav_to_group())



			addedGroup.add_widget(addedButton)
			self.ids.glayout2.add_widget(addedGroup)


	def setGroup(self, instance):
		self.manager.edit_group_behaviour_screen.setGroupName(instance.text[9:-9])

	def setSlotName(self, name):
		self.ids.SlotName.text = name

	def removeSlot(self):
		pass

	def nav_to_group(self):
		self.manager.current = 'edit_group_behaviour_screen_9'

	#triggers on press of any timeline button assigning group number and timeline number to GroupBehaviourScreen.groupNumber and GroupBehaviourScreen.slotNumber
	def group_modification(self,slotNumber):
		#assign group and device number so modifications can be made
		EditGroupBehaviourScreen.slotNumber=slotNumber
		#adds the four tuple to EditGroupBehaviourScreen.groupSettings list if it isnt present, otherwise, loads current switch position and slider amount
		EditGroupBehaviourScreen().add_settings()

	def press_btn(self,instance):
		EditGroupBehaviourScreen.groupNumber=int(instance.text[6])

class DeviceTemplateScreen(Screen):
	pass

class GroupTemplateScreen(Screen):
	currentGroupNo=0
	connectedDevices=[]


	def on_enter(self):
		try:
			#Clear all labels
			#self.ids.groupName.clear_widgets()
			self.ids.devicesConnected.clear_widgets()


			#Add back labels for the group and devices connectedf
			#self.ids.groupName.add_widget(Label(text="Name:",font_size=35))
			#self.ids.groupName.add_widget(Label(text="Group " + str(self.currentGroupNo),font_size=35))
			#NEEDS TO BE CHANGED TO DISPLAY ACTUAL GROUP DATA
			self.ids.groupName.add_widget(Label(text=self.manager.create_group_screen.ids.group_name.text,font_size=20))

			self.ids.devicesConnected.add_widget(Label(text="Status:",font_size=35))
			self.ids.devicesConnected.add_widget(Label(text=str(' Inactive'),font_size=35))

			self.ids.devicelisting.clear_widgets()
			for i in xrange(0,len(ConnectDevicesScreen().applied_list)):
				addedGroup = BoxLayout(size_hint_y=None,height='75sp',orientation='horizontal')

				addedGroup.add_widget(Label(text="Device " + ConnectDevicesScreen().applied_list[i],font_size=10,color=(0,0,0,1)))

				switch=Switch(active=False,id=ConnectDevicesScreen().applied_list[i])
				switch.bind(active=self.switch_on)
				addedGroup.add_widget(switch)

				self.ids.devicelisting.add_widget(addedGroup)
		except Exception:
			print('Error in the on_enter function!')

	def removeGroup(self):
		try:
			del self.manager.groupList[int(self.currentGroupNo)-1]
			for i in range(self.currentGroupNo-1, len(self.manager.groupList), 1):
				self.manager.groupList[i].index -= 1
		except Exception:
			print('Error in the removeGroup function!')

	def removeGroup2(self):

		self.manager.groupList.remove(self.manager.edit_device_groups_screen.matchGroup(self.manager.groupList,self.ids.groupNameLabel.text))



	#saving this for when Group names have to be deleted by name matching
	def removeGroupMatching(self):
		try:
			for i in range(0, len(EditDeviceGroupsScreen().Groups)):
				if self.currentGroupNo == EditDeviceGroupsScreen().Groups[i][0]:
					del (EditDeviceGroupsScreen.Groups[i])
		except Exception:
			print('Error in the removeGroupMatching function!')

	def switch_on(self,instance, value):
		print (instance)
		print (value)

#		if value is active:
#			rint("Checkbox Checked")
#		else:
#			rint("Checkbox Unchecked")


class EditGroupBehaviourScreen(Screen):
	groupNumber = 0
	slotNumber = 0
	switchActive = 0 #not used
	sliderValue = 0
	#groupSettings = [groupNumber-starting at 1,slotNumber-starting at 1,switchActive,sliderValue]
	groupSettings = []

	triggerPercentage = 0
	#triggerSetting = [triggerGroup,affectedGroup,triggerPercentage]
	triggerSetting = []

	#eventlength = length of events(int)
	eventLength = 0

	def on_enter(self):

		self.ids.triggerlisting.clear_widgets()
		#self.ids.SlotNo.text = "Slot " + str(self.manager.select_group_screen.currentSlot)
		for i in xrange(0,len(self.manager.groupList)):
			addedGroup = BoxLayout(size_hint_y=None,height='75sp',orientation='horizontal',id=str(self.manager.groupList[i].index))

			addedGroup.add_widget(Label(text="Group " + str(self.manager.groupList[i].name),font_size=25,color=(0,0,0,1)))

			button=Button(id=str(self.manager.groupList[i].index),text="Apply Trigger",size_hint_x=None,width=175)
			button.bind(on_press=self.add_trigger)

			addedGroup.add_widget(button)

			self.ids.triggerlisting.add_widget(addedGroup)



			print addedGroup.id


	def add_trigger(self, instance):
		groupName = instance.parent.children[1].text[6:]

		if  (0 <= float(self.ids.triggerpercentinput.text) <= 1):
			trigger = (float(self.ids.triggerpercentinput.text), groupName)

		self.manager.matchSlot(self.ids.SlotName.text).matchGroup(self.ids.GroupName.text).triggerList.append(trigger)

	#adds the four tuple to EditGroupBehaviourScreen.groupSettings list if it isnt present. it it already exist return with no change
	def add_settings(self):
		try:
			tempSettings = []
			for i in xrange(0,len(self.groupSettings)):
				if self.groupSettings[i][0]==self.groupNumber and self.groupSettings[i][1]==self.slotNumber:
						return
			tempSettings = [self.groupNumber,self.slotNumber,0,0]
			self.groupSettings.append(tempSettings)
		except Exception:
			print('Error in the add_settings function!')

	#finds and reads four tuple for timeline element to update slider position and switch position
	#for now refresh settings are disabled although save_changes works
	def refresh_settings(self):
		pass

	#reset settings
	def reset_settings(self):
		self.groupSettings = []

	#if save changes button is pressed, update four tuple on group timeline
	def save_changes(self,slotNumber,switchActive,sliderValue,eventlength):
		try:
			#update length of events
			self.eventlength = eventlength
			#find element
			for i in xrange(0,len(self.groupSettings)):

				if self.groupSettings[i][0]==self.groupNumber and self.groupSettings[i][1]==self.slotNumber:
						#update element
						self.groupSettings[i][1] = slotNumber
						self.groupSettings[i][2] = switchActive
						self.groupSettings[i][3] = sliderValue
						print(self.groupSettings)
				for x in xrange(len(self.triggerSetting)):
					if self.triggerSetting[x][0]==self.groupSettings[i][0]:
						j = timelineReader(self.groupSettings[i],1,self.eventlength,str(self.groupSettings[i][0]),len(self.manager.edit_timeline_screen.ids.glayout3.children))
						tmp1 =j.MonthGroupBehavior()
						a=Trigger(self.triggerSetting[x][2],tmp1,1,str(self.groupSettings[i][0]),str(self.triggerSetting[x][1]),len(self.manager.edit_timeline_screen.ids.glayout3.children))
						a.Trigger()
				j = timelineReader(self.groupSettings[i],1,self.eventlength,str(self.groupSettings[i][0]),len(self.manager.edit_timeline_screen.ids.glayout3.children))
				j.MonthGroupBehavior()
		except Exception:
			print('Error in the save_changes function!')

	def save_changes2(self):
		self.manager.matchSlot(self.ids.SlotName.text).matchGroup(self.ids.GroupName.text).eventLength = int(self.ids.eventlengthinput.value)
		self.manager.matchSlot(self.ids.SlotName.text).matchGroup(self.ids.GroupName.text).eventAmount = int(self.ids.eventAmountSlider.value)


	def setSlotName(self, name):
		self.ids.SlotName.text = name
	def setGroupName(self, name):
		self.ids.GroupName.text = name
		print(name)

	#need to finish logic to detect position of switch and feed to four tuple. for now assume switch is active all the time
	def switch_on(self, value):
		if value is True:
			print("Switch On")
		else:
			print("Switch Off")

	#apply trigger



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
	slotList = []
	TLlength = 0.02

	def setTLlength(self, afloat):
		self.TLlength = afloat

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

	def matchSlot(self, aName):
		try:
			for i in xrange(0, len(self.slotList)):
				if aName == self.slotList[i].name:
					return self.slotList[i]
		except Exception:
			print('Error in the matchSlot function!')

	def makeTL(self):
		try:
			TL = TLR(self.slotList, self.TLlength)
			TL.makeTimeline()
		except Exception:
			print('Error in the makeTL function!')


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

	#groupSettings = [groupNumber-starting at 1,slotNumber-starting at 1,switchActive,sliderValue]
	def __init__(self,name,index, devList = [], triggerList = []):
		self.name = name
		self.devList = devList
		self.triggerList = triggerList
		self.index = index
		self.eventLength = 0
		self.eventAmount = 0

	def addDevice(aDevice):
		self.devList.append(aDevice)
	def addTrigger(aTrigger):
		self.triggerList.append(aTrigger)

	def signalGroup(self):
		pass
		# TODO handle the event triggering
class Slot():

	def __init__(self, aName):
		self.name = aName
		self.groupList = []
	def addGroup(self, aGroup):
		self.groupList.append(aGroup)
	def addGroupList(self, aGroupList):
		self.groupList = aGroupList[:]

	def matchGroup(self, aName):

		for i in xrange(0, len(self.groupList)):
			if aName == self.groupList[i].name:
				return self.groupList[i]


class LoadingScreen(Screen):
	def on_enter(self):
		pass

class SoundCloutApp(App):
	def build(self):
		return Manager(transition=WipeTransition())

if  __name__=='__main__':

	SoundCloutApp().run()
