from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException


class DragnDrop:

    # constructor to initialize url and driver
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # method to drag and drop object
    def dragObject(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
            # action chains are used to perform drag and drop of an object
            action = ActionChains(self.driver)
            # drag and drop objects are present in iframe. so need to switch the control to iframe
            self.driver.switch_to.frame(0)
            # trying to find objects using id
            source = self.driver.find_element(By.ID, value="draggable")
            target = self.driver.find_element(By.ID, value="droppable")
            # checking both objects if they are displayed/enabled or not
            if source.is_displayed() and target.is_displayed():
                if source.is_enabled() and target.is_enabled():
                    # using action chains performing drag and drop of objects
                    action.drag_and_drop(source, target).perform()
            # waiting for some time to check if objects are dragged and dropped
            self.driver.implicitly_wait(10)
        except(NoSuchElementException, ElementNotVisibleException) as e:
            print("Error: ", e)


url = "https://jqueryui.com/droppable/"
dd = DragnDrop(url)
dd.dragObject()
