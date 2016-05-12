from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper

class Application():
    def __init__(self, browser, baseUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.baseUrl = baseUrl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        # open homepage
        if not (wd.current_url.endswith("mantisbt-1.2.19/login_page.php") and len(wd.find_element_by_css_selector('input[type="submit"]')) > 0):
            wd.get(self.baseUrl)

    def destroy(self):
        self.wd.quit()