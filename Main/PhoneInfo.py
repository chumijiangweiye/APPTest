# -*- encoding:utf-8 -*-
import unittest
from appium import webdriver
import os
import time

class Login(unittest.TestCase):
    def setUp(self):
        desired_cups = {}
        #设备平台
        desired_cups['platformName'] = 'Android'
        #设备系统版本
        #使用命令adb shell getprop ro.build.version.release
        desired_cups['platformVersion'] = '6.0.1'
        #设备名称
        #使用命令adb devices -l
        desired_cups['deviceName'] = 'Redmi_3S'

        desired_cups['appPackage'] = 'com.grandsoft.intercom'
        desired_cups['appActivity'] = 'com.grandsoft.intercom.SplashActivity'
        #如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

        #启动app
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_cups)

        #启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        time.sleep(3)