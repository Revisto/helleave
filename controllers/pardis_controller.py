from selenium import webdriver
from validator_collection import is_not_empty
from fake_useragent import UserAgent
from time import sleep

class PardisSelenium:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.domain = "https://www.helli4.ir/"
        self.login_url = self.domain + "portal/user/"
        self.classes_url = self.domain + "pds/vclasses.php"

    def log_in(self, user_credentials):
        print("Logging in...")
        self.driver.get(self.login_url)
        print("Loading login page...")
        login_form = self.driver.find_elements_by_id("user-login")
        if not is_not_empty(login_form):
            print("Already logged in.")
            return True
        login_form = login_form[0]
        
        print("Putting in username...")
        username = login_form.find_element_by_id("edit-name")
        username.send_keys(user_credentials["username"])
        print("Putting in password...")
        password = login_form.find_element_by_id("edit-pass")
        password.send_keys(user_credentials["password"])
        print("Submitting login form...")
        login_button = login_form.find_element_by_id("edit-submit")
        login_button.click()
        return True

    def go_to_adobe_connect(self):
        print("Changing user agent and platform so fucking adobe connect doesn't stop me from loggin in...")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": UserAgent().chrome, "platform": "Android"})
        print("Going to classes page...")
        self.driver.get(self.classes_url)
        print("Clicking on user class...")
        user_class_button = self.driver.find_elements_by_class_name("form-control")[0]
        user_class_button.click()
        sleep(5)
        while True:
            self.driver.refresh()
            sleep(10)
            print("Clicking on open in browser button...")
            try:
                open_in_browser_button = self.driver.find_elements_by_class_name("button-content")[0]
                open_in_browser_button.click()
                break
            except:
                pass
            
        return True

    def go_to_class(self, user_credentials):
        self.log_in(user_credentials)
        self.go_to_adobe_connect()
