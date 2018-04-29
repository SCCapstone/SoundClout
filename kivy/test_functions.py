import unittest
import sys,os.path
import kivy
from kivy.tests.common import GraphicUnitTest
from timelinereader import *
from triggers import *
from plot import *
from reroll import *

 # testing based on tests from https://github.com/KeyWeeUsr/KivyUnitTest/blob/master/kivyunittest/examples/test_text.py

class FunctionTests(unittest.TestCase):
    def test_timelinereader(self):
        newList=[0,1,1,0]
        j = timelineReader(newList,.2,.01,"group1",100)
        a = j.MonthGroupBehavior()
        assert isinstance(a,basestring)== True
    def test_trigger(self):
        newList=[1,1,1,12]
        j = timelineReader(newList,1,1,"1",1)
        tmp1=j.MonthGroupBehavior()
        a = Trigger(100,tmp1,3,'3',3,3)
        b= a.Trigger()
        assert b != None
    def test_plot(self):
        z= ['group1']
        plot(10,1,z)
        assert os.path.exists('timeline.png') == True
    def test_reroll(self):
        a =reroll(20)
        assert a==0 or a==1

import os
import sys
import time
import os.path as op
from functools import partial
from kivy.clock import Clock
from main import *

main_path = op.dirname(op.dirname(op.abspath(__file__)))
sys.path.append(main_path)


#from main import Device

class TestDevice(unittest.TestCase):
   
    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        app.my_button.dispatch('on_release')
        self.assertEqual('Hello Test', app.my_button.text)

        app.stop()

    def test_file_screen(self):
        
        app = Device()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, .000001)
        app.__init__()

#from main import HomeScreen

class TestHomeScreen(unittest.TestCase):
   
    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        app.my_button.dispatch('on_release')
        self.assertEqual('Hello Test', app.my_button.text)

        app.stop()

    def test_file_screen(self):
        
        app = HomeScreen()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, .000001)
        app.__init__()

#from main import RunScreen

class TestRunScreen(unittest.TestCase):
   
    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        app.my_button.dispatch('on_release')
        self.assertEqual('Hello Test', app.my_button.text)

        app.stop()

    def test_file_screen(self):
        
        app = RunScreen()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, .000001)
        app.__init__()


class TestDeviceTesterScreen(unittest.TestCase):
   
    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        app.my_button.dispatch('on_release')
        self.assertEqual('Hello Test', app.my_button.text)

        app.stop()

    def test_file_screen(self):
        
        app = DeviceTesterScreen()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, .000001)
        app.__init__()


class TestConnectDevicesScreen(unittest.TestCase):
   
    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        app.my_button.dispatch('on_release')
        self.assertEqual('Hello Test', app.my_button.text)

        app.stop()

    def test_file_screen(self):
        
        app = ConnectDevicesScreen()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, .000001)
        app.__init__()


class TestEditDeviceGroupsScreen(unittest.TestCase):
   
    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        app.my_button.dispatch('on_release')
        self.assertEqual('Hello Test', app.my_button.text)

        app.stop()

    def test_file_screen(self):
        
        app = EditDeviceGroupsScreen()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, .000001)
        app.__init__()


class TestEditTimelineScreen(unittest.TestCase):
   
    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        app.my_button.dispatch('on_release')
        self.assertEqual('Hello Test', app.my_button.text)

        app.stop()

    def test_file_screen(self):
        
        app = EditTimelineScreen()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, .000001)
        app.__init__()


class TestSelectGroupScreen(unittest.TestCase):
   
    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        app.my_button.dispatch('on_release')
        self.assertEqual('Hello Test', app.my_button.text)

        app.stop()

    def test_file_screen(self):
        
        app = SelectGroupScreen()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, .000001)
        app.__init__()


class TestGroupTemplateScreen(unittest.TestCase):
   
    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        app.my_button.dispatch('on_release')
        self.assertEqual('Hello Test', app.my_button.text)

        app.stop()

    def test_file_screen(self):
        
        app = GroupTemplateScreen()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, .000001)
        app.__init__()


class TestEditGroupBehaviourScreen(unittest.TestCase):
   
    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something
        app.my_button.dispatch('on_release')
        self.assertEqual('Hello Test', app.my_button.text)

        app.stop()

    def test_file_screen(self):
        
        app = EditGroupBehaviourScreen()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, .000001)
        app.__init__()


if __name__ == '__main__':
    unittest.main()