# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class TestDefaultSuite():
  def setup_method(self):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    self.driver = webdriver.Chrome(chrome_options=chrome_options)
    #self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_algeria(self):
    # Test name: Algeria
    # Step # | name | target | value
    # 1 | open | https://africacdc.org/covid-19/ | 
    self.driver.get("https://africacdc.org/covid-19/")
    # 2 | selectFrame | index=0 | 
    self.driver.switch_to.frame(0)
    # 3 | waitForElementVisible | css=circle:nth-child(9) | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "circle:nth-child(9)")))
    # 4 | click | css=circle:nth-child(9) | 
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(9)").click()
    # 5 | waitForElementVisible | css=tr:nth-child(8) .esriNumericValue | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue")))
    # 6 | storeText | css=tr:nth-child(8) .esriNumericValue | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    # 7 | click | css=.map-toolbar-left > div:nth-of-type(2) > div div:nth-of-type(2) > a:nth-of-type(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".map-toolbar-left > div:nth-of-type(2) > div div:nth-of-type(2) > a:nth-of-type(2)").click()
    # 8 | storeText | css=.avenir-bold | country
    self.vars["country"] = self.driver.find_element(By.CSS_SELECTOR, ".avenir-bold").text
    print(self.vars["country"], "done")
    # 9 | close |  | 
    self.driver.close()
  
  def test_other(self):
    # Test name: Other
    # Step # | name | target | value
    # 1 | open | https://africacdc.org/covid-19/ | 
    self.driver.get("https://africacdc.org/covid-19/")
    # 2 | selectFrame | index=0 | 
    self.driver.switch_to.frame(0)
    # 3 | waitForElementVisible | css=circle:nth-child(9) | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "circle:nth-child(24)")))
    # 4 | click | css=circle:nth-child(9) | 
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(24)").click()
    # 5 | waitForElementVisible | css=tr:nth-child(8) .esriNumericValue | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue")))
    # 6 | storeText | css=tr:nth-child(8) .esriNumericValue | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    # 7 | click | css=.map-toolbar-left > div:nth-of-type(2) > div div:nth-of-type(2) > a:nth-of-type(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".map-toolbar-left > div:nth-of-type(2) > div div:nth-of-type(2) > a:nth-of-type(2)").click()
    # 8 | storeText | css=.avenir-bold | country
    self.vars["country"] = self.driver.find_element(By.CSS_SELECTOR, ".avenir-bold").text
    print(self.vars["country"], "done")
    # 9 | close |  | 
    self.driver.close()
  
