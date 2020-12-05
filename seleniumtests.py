from selenium import webdriver
import pyautogui,time
class Duck:
    def __init__(self,driver):
        
        self.driver=driver
        self.url='https://duckduckgo.com'
        self.search_bar_id="search_form_input_homepage"
        self.search_button="btnK"
        self.first_link_class="result__url__domain"
    def navigate (self):
         
         self.driver.get(self.url)
    
    def search(self,nome='None'):
        self.driver.find_element_by_id(self.search_bar_id).send_keys(nome)
        #self.driver.find_element_by_name(self.search_bar).send_keys()
        pyautogui.typewrite('\n')


    def textconvert(self):
        time.sleep(4)
        message=self.driver.find_element_by_class_name(self.first_link_class).text
        return str(message)

class Wiki:

    def __init__(self,driver):

        self.driver=driver
        self.url='https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal'
        
ff=webdriver.Firefox()
g=Duck(ff)
with open (r"C:\Users\Dell\Documents\documentos\marcas.txt",'r') as f:
    with open (r"C:\Users\Dell\Documents\documentos\links.txt", 'w' ) as fw:
        for line in f : 
            g.navigate()
            g.search(line)
            fw.write((line) + g.textconvert()+' \n')