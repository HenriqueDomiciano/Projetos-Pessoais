from selenium import webdriver
import time,pyautogui

class Youtube_dowload():  
    def __init__(self,driver):
        self.driver=driver
        self.url=""
        self.button_class=''
        self.link_box_name=''
        self.waiting_bar=''
        self.driver.f
    
    def navigate_to_starter(self):
        self.driver.get(self.url)
    
    def enter_url(self,link=None):
        self.driver.find_element_by_name(self.link_box_name).send_keys(link)
        pyautogui.typewrite('\n')
        time.sleep(4)


