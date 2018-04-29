import unittest
import sys,os.path
sys.path.insert(0, '/home/hb/Downloads/SoundClout-master/kivy')
import kivy
from timelinereader import *
from triggers import *
from plot import *
from reroll import *

def test_timelinereader():
    newList=[0,1,1,0]
    j = timelineReader(newList,.2,.01,"group1",100)
    a = j.MonthGroupBehavior()
    assert isinstance(a,basestring)== True
def test_trigger():
    newList=[1,1,1,12]
    j = timelineReader(newList,1,1,"1",1)
    tmp1=j.MonthGroupBehavior()
    a = Trigger(100,tmp1,3,'3',3,3)
    b= a.Trigger()
    assert b != None
def test_plot():
    z= ['group1']
    plot(10,1,z)
    assert os.path.exists('timeline.png') == True
def test_reroll():
    a =reroll(20)
    assert a==0 or a==1
