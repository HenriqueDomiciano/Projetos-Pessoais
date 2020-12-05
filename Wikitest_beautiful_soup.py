from selenium import webdriver
from bs4 import BeautifulSoup
import os,time,requests,lxml,csv
class Wikipedia :
    def __init__(self,driver):

        self.driver=driver 
        self.url = 'https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal'
        self.search_box='//*[@id="searchInput"]' #xpath
        self.search_button='//*[@id="searchButton"]'

    def navigate(self):

        self.driver.get(self.url)

    def search(self,name=None):

        self.driver.find_element_by_xpath(self.search_box).send_keys(name)
        self.driver.find_element_by_xpath(self.search_button).click()
        return self.driver.current_url

web_driver=webdriver.Firefox()
wiki=Wikipedia(web_driver)
wiki.navigate()
vari=[]

with open(r'C:\Users\Dell\Documents\documentos\marcas.txt','r') as f:
    for lines in f :
        url=wiki.search(lines)
        new_url=requests.get(url)
        new_url_bytes=new_url.text
        soup=BeautifulSoup(new_url_bytes,'lxml')
        text=BeautifulSoup.get_text(soup)
        vari.append([url,str(lines),])
        

        with open (r'C:\Users\Dell\Documents\documentos\contents' +'\\' + str(''.join(lines.split())) + '.txt', 'x', encoding='utf-8') as tw:
            tw.write(text)

with open (r'C:\Users\Dell\Documents\documentos\links.csv','a', encoding='utf-8',newline='') as fw :
    labels=['url','empresa']
    ar=csv.writer(fw)
    ar.writerow(labels)
    ar.writerows(vari) 
    print(vari)
        
        

'''
        Nao funciona nao sei pq ? 
        new_pdf = open (local,'w+b')
        pisa_status=pisa.CreatePDF(new_url_bytes,dest=new_pdf)
        new_pdf.close()
        i=i+
'''
