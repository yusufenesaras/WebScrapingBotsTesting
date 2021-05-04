import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

baslik = input("Ekşi sözlükte aramak istediğiniz başlığı girin: ")

options = webdriver.ChromeOptions()
options.add_argument('headless') #chrome sekmesini arkaplana atıyoruz.

url = "https://eksisozluk.com/"

browser = webdriver.Chrome(options=options)

time.sleep(2)
browser.get(url)

input_area = browser.find_element_by_xpath("//*[@id='search-textbox']")
button = browser.find_element_by_xpath("//*[@id='search-form']/button")

time.sleep(2)

input_area.send_keys(baslik)
time.sleep(2)

button.click()

time.sleep(2)
url = browser.current_url
source = browser.page_source

soup = bs(source,"html.parser")

try:
    page_count = len(soup.find("div",{"class":"clearfix sub-title-container"}).find("div",{"class":"pager"}).find_all("option"))
except:
    page_count = 1

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
for i in range(1,page_count+1):
    response = requests.get(url+ "?p=" + str(i),headers=headers)
    time.sleep(2)

    soup = bs(response.content,"html.parser")
    entry_divs = soup.find_all("div",{"class":"content"})

    for entry in entry_divs:
        print(entry.text)
        footer = entry.findNext("footer")
        author = footer.find_all("a")[1].text
        print("Yazar: "+ author)
        print("*"*100)

browser.close()
