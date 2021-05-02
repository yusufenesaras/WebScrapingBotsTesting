from selenium import webdriver
import time
from githubUserInfo import username, password

# install chromedriver.exe or any browser

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []


    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()


    def getFollowers(self):
        self.browser.get("https://github.com/y-enesaras?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")

        for i in items:
            self.followers.append(i.find_element_by_css_selector(".Link--secondary.pl-1").text)

github = Github(username,password)
github.signIn()
github.getFollowers()
print(github.followers)














