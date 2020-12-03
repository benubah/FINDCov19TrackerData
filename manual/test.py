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
    #chrome_options.add_argument("--window-size=1920,1080")
    self.driver = webdriver.Chrome(chrome_options=chrome_options)
    #self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_australia(self):
    # Test name: Australia
    # Step # | name | target | value
    # 1 | open | https://www.health.gov.au/resources/total-covid-19-tests-conducted-and-results | 
    self.driver.get("https://www.health.gov.au/resources/total-covid-19-tests-conducted-and-results")
    # 2 | waitForElementNotPresent | css=.ng-scope:nth-child(1) > .ng-binding:nth-child(2) | 30000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .ng-binding:nth-child(2)")))
    # 3 | storeText | css=.ng-scope:nth-child(1) > .ng-binding:nth-child(2) | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .ng-binding:nth-child(2)").text
    self.vars["country"] = "Australia"
    # 4 | close |  | 
    self.driver.close()
  
  def test_bosniaandHerzegovina(self):
    # Test name: BosniaandHerzegovina
    # Step # | name | target | value
    # 1 | open | https://covid-19.ba/ | 
    self.driver.get("https://covid-19.ba/")
    # 2 | waitForElementVisible | id=total_tested_positive | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.ID, "total_tested_positive")))
    # 3 | storeText | id=total_tested_positive | tests
    self.vars["tests"] = self.driver.find_element(By.ID, "total_tested_positive").text
    self.vars["country"] = "BosniaandHerzegovina"
    # 4 | close |  | 
    self.driver.close()
  
  def test_brunei(self):
    # Test name: Brunei
    # Step # | name | target | value
    # 1 | open | http://www.moh.gov.bn/Lists/Latest%20news/AllItems.aspx | 
    self.driver.get("http://www.moh.gov.bn/Lists/Latest%20news/AllItems.aspx")
    # 2 | click | css=.ms-listlink:nth-of-type(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".ms-listlink:nth-of-type(1)").click()
    # 3 | waitForElementVisible | css=.ms-rteTable-default:nth-child(17) .ms-rteTable-default:nth-child(2) > strong | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ms-rteTable-default:nth-child(17) .ms-rteTable-default:nth-child(2) > strong")))
    # 4 | storeText | css=.ms-rteTable-default:nth-child(17) .ms-rteTable-default:nth-child(2) > strong | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".ms-rteTable-default:nth-child(17) .ms-rteTable-default:nth-child(2) > strong").text
    self.vars["country"] = "Brunei"
    # 5 | close |  | 
    self.driver.close()
  
  def test_bulgaria(self):
    # Test name: Bulgaria
    # Step # | name | target | value
    # 1 | open | https://coronavirus.bg/ | 
    self.driver.get("https://coronavirus.bg/")
    # 2 | waitForElementVisible | css=.col-lg-3:nth-child(1) > .statistics-value | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".col-lg-3:nth-child(1) > .statistics-value")))
    # 3 | storeText | css=.col-lg-3:nth-child(1) > .statistics-value | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".col-lg-3:nth-child(1) > .statistics-value").text
    self.vars["country"] = "Bulgaria"
    # 4 | close |  | 
    self.driver.close()
  
  def test_canada(self):
    # Test name: Canada
    # Step # | name | target | value
    # 1 | open | https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html | 
    self.driver.get("https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html")
    # 2 | waitForElementVisible | css=.numTested | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".numTested")))
    # 3 | storeText | css=.numTested | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".numTested").text
    self.vars["country"] = "Canada"
    # 4 | close |  | 
    self.driver.close()
  
  def test_estonia(self):
    # Test name: Estonia
    # Step # | name | target | value
    # 1 | open | https://koroonakaart.ee/et | 
    self.driver.get("https://koroonakaart.ee/et")
    # 2 | waitForElementVisible | css=.row:nth-child(2) > .statsbar-item:nth-child(4) > h1 | 30000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(2) > .statsbar-item:nth-child(4) > h1")))
    # 3 | storeText | css=.row:nth-child(2) > .statsbar-item:nth-child(4) > h1 | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(2) > .statsbar-item:nth-child(4) > h1").text
    self.vars["country"] = "Estonia"
    # 4 | close |  | 
    self.driver.close()
  
  def test_france(self):
    # Test name: France
    # Step # | name | target | value
    # 1 | open | https://dashboard.covid19.data.gouv.fr/suivi-des-tests?location=FRA | 
    self.driver.get("https://dashboard.covid19.data.gouv.fr/suivi-des-tests?location=FRA")
    # 2 | waitForElementVisible | css=.counter-container > .jsx-792689997 | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".counter-container > .jsx-792689997")))
    # 3 | storeText | css=.counter-container > .jsx-792689997 | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".counter-container > .jsx-792689997").text
    self.vars["country"] = "France"
    # 4 | close |  | 
    self.driver.close()
  
  def test_hungary(self):
    # Test name: Hungary
    # Step # | name | target | value
    # 1 | open | https://koronavirus.gov.hu/#aktualis | 
    self.driver.get("https://koronavirus.gov.hu/#aktualis")
    # 2 | waitForElementVisible | id=content-mintavetel | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.ID, "content-mintavetel")))
    # 3 | storeText | id=content-mintavetel | tests
    self.vars["tests"] = self.driver.find_element(By.ID, "content-mintavetel").text
    self.vars["country"] = "Hungary"
    # 4 | close |  | 
    self.driver.close()
  
  def test_india(self):
    # Test name: India
    # Step # | name | target | value
    # 1 | open | https://www.icmr.gov.in/ | 
    self.driver.get("https://www.icmr.gov.in/")
    # 2 | waitForElementVisible | css=.col-12:nth-child(1) > .single-cool-fact h2 | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".col-12:nth-child(1) > .single-cool-fact h2")))
    # 3 | storeText | css=.col-12:nth-child(1) > .single-cool-fact h2 | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(1) > .single-cool-fact h2").text
    self.vars["country"] = "India"
    # 4 | close |  | 
    self.driver.close()
  
  def test_ireland(self):
    # Test name: Ireland
    # Step # | name | target | value
    # 1 | open | https://covid19ireland-geohive.hub.arcgis.com/pages/hospitals-icu--testing | 
    self.driver.get("https://covid19ireland-geohive.hub.arcgis.com/pages/hospitals-icu--testing")
    # 2 | waitForElementVisible | css=#ember142 .ss-value | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#ember142 .ss-value")))
    # 3 | storeText | css=#ember142 .ss-value | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, "#ember142 .ss-value").text
    self.vars["country"] = "Ireland"
    # 4 | close |  | 
    self.driver.close()
  
  def test_latvia(self):
    # Test name: Latvia
    # Step # | name | target | value
    # 1 | open | https://infogram.com/covid-19-izplatiba-latvija-1hzj4ozwvnzo2pw | 
    self.driver.get("https://infogram.com/covid-19-izplatiba-latvija-1hzj4ozwvnzo2pw")
    # 2 | waitForElementVisible | css=.InfographicEditor-Contents-Item:nth-child(11) .igc-textual-figure > div | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".InfographicEditor-Contents-Item:nth-child(11) .igc-textual-figure > div")))
    # 3 | storeText | css=.InfographicEditor-Contents-Item:nth-child(11) .igc-textual-figure > div | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".InfographicEditor-Contents-Item:nth-child(11) .igc-textual-figure > div").text
    self.vars["country"] = "Latvia"
    # 4 | close |  | 
    self.driver.close()
  
  def test_lithuania(self):
    # Test name: Lithuania
    # Step # | name | target | value
    # 1 | open | https://osp.stat.gov.lt/praejusios-paros-covid-19-statistika | 
    self.driver.get("https://osp.stat.gov.lt/praejusios-paros-covid-19-statistika")
    # 2 | waitForElementVisible | css=tr:nth-child(13) > td:nth-child(1) span > span | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(13) > td:nth-child(1) span > span")))
    # 3 | storeText | css=tr:nth-child(13) > td:nth-child(1) span > span | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(13) > td:nth-child(1) span > span").text
    self.vars["country"] = "Lithuania"
    # 4 | close |  | 
    self.driver.close()
  
  def test_nepal(self):
    # Test name: Nepal
    # Step # | name | target | value
    # 1 | open | https://covid19.mohp.gov.np/ | 
    self.driver.get("https://covid19.mohp.gov.np/")
    # 2 | waitForElementVisible | css=.ant-col-md-24 .ant-typography:nth-child(2) | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ant-col-md-24 .ant-typography:nth-child(2)")))
    # 3 | storeText | css=.ant-col-md-24 .ant-typography:nth-child(2) | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".ant-col-md-24 .ant-typography:nth-child(2)").text
    self.vars["country"] = "Nepal"
    # 4 | close |  | 
    self.driver.close()
  
  def test_newZealand(self):
    # Test name: NewZealand
    # Step # | name | target | value
    # 1 | open | https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-testing-data | 
    self.driver.get("https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-testing-data")
    # 2 | waitForElementVisible | css=.table-responsive:nth-child(9) tr:nth-child(1) > td | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".table-responsive:nth-child(9) tr:nth-child(1) > td")))
    # 3 | storeText | css=.table-responsive:nth-child(9) tr:nth-child(1) > td | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".table-responsive:nth-child(9) tr:nth-child(1) > td").text
    self.vars["country"] = "NewZealand"
    # 4 | close |  | 
    self.driver.close()
  
  def test_northMacedonia(self):
    # Test name: NorthMacedonia
    # Step # | name | target | value
    # 1 | open | https://datastudio.google.com/embed/u/0/reporting/9f5104d0-12fd-4e16-9a11-993685cfd40f/page/1M | 
    self.driver.get("https://datastudio.google.com/embed/u/0/reporting/9f5104d0-12fd-4e16-9a11-993685cfd40f/page/1M")
    # 2 | waitForElementVisible | css=.cd-vmd90p9a8b .valueLabel | 30000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".cd-vmd90p9a8b .valueLabel")))
    # 3 | storeText | css=.cd-vmd90p9a8b .valueLabel | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".cd-vmd90p9a8b .valueLabel").text
    self.vars["country"] = "NorthMacedonia"
    # 4 | close |  | 
    self.driver.close()
  
  def test_norway(self):
    # Test name: Norway
    # Step # | name | target | value
    # 1 | open | https://www.fhi.no/en/id/infectious-diseases/coronavirus/daily-reports/daily-reports-COVID19/ | 
    self.driver.get("https://www.fhi.no/en/id/infectious-diseases/coronavirus/daily-reports/daily-reports-COVID19/")
    # 2 | waitForElementVisible | css=.c-key-figure:nth-child(1) .c-key-figure__number > span | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".c-key-figure:nth-child(1) .c-key-figure__number > span")))
    # 3 | storeText | css=.c-key-figure:nth-child(1) .c-key-figure__number > span | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".c-key-figure:nth-child(1) .c-key-figure__number > span").text
    self.vars["country"] = "Norway"
    # 4 | close |  | 
    self.driver.close()
  
  def test_occupiedPalestinianterritory(self):
    # Test name: occupiedPalestinianterritory
    # Step # | name | target | value
    # 1 | open | https://corona.ps/ | 
    self.driver.get("https://corona.ps/")
    # 2 | waitForElementVisible | css=.roundbox:nth-child(1) > div:nth-child(2) | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".roundbox:nth-child(1) > div:nth-child(2)")))
    # 3 | storeText | css=.roundbox:nth-child(1) > div:nth-child(2) | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".roundbox:nth-child(1) > div:nth-child(2)").text
    self.vars["country"] = "occupiedPalestinianterritory"
    # 4 | close |  | 
    self.driver.close()
  
  def test_qatar(self):
    # Test name: Qatar
    # Step # | name | target | value
    # 1 | open | https://covid19.moph.gov.qa/EN/Pages/default.aspx# | 
    self.driver.get("https://covid19.moph.gov.qa/EN/Pages/default.aspx#")
    # 2 | waitForElementVisible | id=strgPeopleTested | 30000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.ID, "strgPeopleTested")))
    # 3 | storeText | id=strgPeopleTested | tests
    self.vars["tests"] = self.driver.find_element(By.ID, "strgPeopleTested").text
    self.vars["country"] = "Qatar"
    # 4 | close |  | 
    self.driver.close()
  
  def test_republicofKorea(self):
    # Test name: RepublicofKorea
    # Step # | name | target | value
    # 1 | open | http://ncov.mohw.go.kr/en/ | 
    self.driver.get("http://ncov.mohw.go.kr/en/")
    # 2 | waitForElementVisible | css=li:nth-child(1) > .misil_r > span | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-child(1) > .misil_r > span")))
    # 3 | storeText | css=li:nth-child(1) > .misil_r > span | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .misil_r > span").text
    self.vars["country"] = "RepublicofKorea"
    # 4 | close |  | 
    self.driver.close()
  
  def test_southAfrica(self):
    # Test name: SouthAfrica
    # Step # | name | target | value
    # 1 | open | https://gis.nicd.ac.za/portal/apps/opsdashboard/index.html#/0ec12f471aaa4055999366669b38482d | 
    self.driver.get("https://gis.nicd.ac.za/portal/apps/opsdashboard/index.html#/0ec12f471aaa4055999366669b38482d")
    # 2 | waitForElementVisible | css=#ember232 text | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#ember232 text")))
    # 3 | storeText | css=#ember232 text | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, "#ember232 text").text
    self.vars["country"] = "SouthAfrica"
    # 4 | close |  | 
    self.driver.close()
  
  def test_singapore(self):
    # Test name: Singapore
    # Step # | name | target | value
    # 1 | open | https://www.moh.gov.sg/covid-19 | 
    self.driver.get("https://www.moh.gov.sg/covid-19")
    # 2 | waitForElementVisible | css=#ContentPlaceHolder_contentPlaceholder_C095_Col00 b | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#ContentPlaceHolder_contentPlaceholder_C095_Col00 b")))
    # 3 | storeText | css=#ContentPlaceHolder_contentPlaceholder_C095_Col00 b | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder_contentPlaceholder_C095_Col00 b").text
    self.vars["country"] = "Singapore"
    # 4 | close |  | 
    self.driver.close()
  
  def test_slovakia(self):
    # Test name: Slovakia
    # Step # | name | target | value
    # 1 | open | https://korona.gov.sk/ | 
    self.driver.get("https://korona.gov.sk/")
    # 2 | waitForElementVisible | css=#block_5e9990e25ffff .govuk-heading-l | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#block_5e9990e25ffff .govuk-heading-l")))
    # 3 | storeText | css=#block_5e9990e25ffff .govuk-heading-l | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, "#block_5e9990e25ffff .govuk-heading-l").text
    self.vars["country"] = "Slovakia"
    # 4 | close |  | 
    self.driver.close()
  
  def test_sriLanka(self):
    # Test name: SriLanka
    # Step # | name | target | value
    # 1 | open | https://www.hpb.health.gov.lk/en | 
    self.driver.get("https://www.hpb.health.gov.lk/en")
    # 2 | waitForElementVisible | css=.total-count | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".total-count")))
    # 3 | storeText | css=.total-count | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".total-count").text
    self.vars["country"] = "SriLanka"
    # 4 | close |  | 
    self.driver.close()
  
  def test_turkey(self):
    # Test name: Turkey
    # Step # | name | target | value
    # 1 | open | https://covid19.saglik.gov.tr/ | 
    self.driver.get("https://covid19.saglik.gov.tr/")
    # 2 | waitForElementVisible | css=.toplam-test-sayisi | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".toplam-test-sayisi")))
    # 3 | storeText | css=.toplam-test-sayisi | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".toplam-test-sayisi").text
    self.vars["country"] = "Turkey"
    # 4 | close |  | 
    self.driver.close()
  
  def test_unitedArabEmirates(self):
    # Test name: UnitedArabEmirates
    # Step # | name | target | value
    # 1 | open | https://fcsa.gov.ae/en-us/Pages/Covid19/UAE-Covid-19-Updates.aspx | 
    self.driver.get("https://fcsa.gov.ae/en-us/Pages/Covid19/UAE-Covid-19-Updates.aspx")
    # 2 | waitForElementVisible | css=.total_tests > .numbers | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".total_tests > .numbers")))
    # 3 | storeText | css=.total_tests > .numbers | tests
    self.vars["tests"] = self.driver.find_element(By.CSS_SELECTOR, ".total_tests > .numbers").text
    self.vars["country"] = "UnitedArabEmirates"
    # 4 | close |  | 
    self.driver.close()
  
  def test_unitedKingdom(self):
    # Test name: UnitedKingdom
    # Step # | name | target | value
    # 1 | open | https://coronavirus.data.gov.uk/testing | 
    self.driver.get("https://coronavirus.data.gov.uk/testing")
    # 2 | waitForElementVisible | id=value-item-virus_tests_conducted-total-cumvirustests-1_modal | 300000
    WebDriverWait(self.driver, 300000).until(expected_conditions.visibility_of_element_located((By.ID, "value-item-virus_tests_conducted-total-cumvirustests-1_modal")))
    # 3 | storeText | id=value-item-virus_tests_conducted-total-cumvirustests-1_modal | tests
    self.vars["tests"] = self.driver.find_element(By.ID, "value-item-virus_tests_conducted-total-cumvirustests-1_modal").text
    self.vars["country"] = "UnitedKingdom"
    # 4 | close |  | 
    self.driver.close()
  
country_list = []

australia = TestDefaultSuite()
australia.setup_method()
australia.test_australia()
australia.teardown_method()
australia.vars

country_list.append(australia.vars)

bosniaandHerzegovina = TestDefaultSuite()
bosniaandHerzegovina.setup_method()
bosniaandHerzegovina.test_bosniaandHerzegovina()
bosniaandHerzegovina.teardown_method()
bosniaandHerzegovina.vars

country_list.append(bosniaandHerzegovina.vars)

#brunei = TestDefaultSuite()
#brunei.setup_method()
#brunei.test_brunei()
#brunei.teardown_method()
#brunei.vars

#country_list.append(brunei.vars)

bulgaria = TestDefaultSuite()
bulgaria.setup_method()
bulgaria.test_bulgaria()
bulgaria.teardown_method()
bulgaria.vars

country_list.append(bulgaria.vars)

canada = TestDefaultSuite()
canada.setup_method()
canada.test_canada()
canada.teardown_method()
canada.vars

country_list.append(canada.vars)

estonia = TestDefaultSuite()
estonia.setup_method()
estonia.test_estonia()
estonia.teardown_method()
estonia.vars
country_list.append(estonia.vars)

#france = TestDefaultSuite()
#france.setup_method()
#france.test_france()
#france.teardown_method()
#france.vars
#country_list.append(france.vars)

hungary = TestDefaultSuite()
hungary.setup_method()
hungary.test_hungary()
hungary.teardown_method()
hungary.vars
country_list.append(hungary.vars)

india = TestDefaultSuite()
india.setup_method()
india.test_india()
india.teardown_method()
india.vars
country_list.append(india.vars)

ireland = TestDefaultSuite()
ireland.setup_method()
ireland.test_ireland()
ireland.teardown_method()
ireland.vars
country_list.append(ireland.vars)

latvia = TestDefaultSuite()
latvia.setup_method()
latvia.test_latvia()
latvia.teardown_method()
latvia.vars
country_list.append(latvia.vars)

lithuania = TestDefaultSuite()
lithuania.setup_method()
lithuania.test_lithuania()
lithuania.teardown_method()
lithuania.vars
country_list.append(lithuania.vars)

nepal = TestDefaultSuite()
nepal.setup_method()
nepal.test_nepal()
nepal.teardown_method()
nepal.vars
country_list.append(nepal.vars)

newZealand = TestDefaultSuite()
newZealand.setup_method()
newZealand.test_newZealand()
newZealand.teardown_method()
newZealand.vars
country_list.append(newZealand.vars)

#northMacedonia = TestDefaultSuite()
#northMacedonia.setup_method()
#northMacedonia.test_northMacedonia()
#northMacedonia.teardown_method()
#northMacedonia.vars
#country_list.append(northMacedonia.vars)

norway = TestDefaultSuite()
norway.setup_method()
norway.test_norway()
norway.teardown_method()
norway.vars
country_list.append(norway.vars)

occupiedPalestinianterritory = TestDefaultSuite()
occupiedPalestinianterritory.setup_method()
occupiedPalestinianterritory.test_occupiedPalestinianterritory()
occupiedPalestinianterritory.teardown_method()
occupiedPalestinianterritory.vars
country_list.append(occupiedPalestinianterritory.vars)

qatar = TestDefaultSuite()
qatar.setup_method()
qatar.test_qatar()
qatar.teardown_method()
qatar.vars
country_list.append(qatar.vars)

republicofKorea = TestDefaultSuite()
republicofKorea.setup_method()
republicofKorea.test_republicofKorea()
republicofKorea.teardown_method()
republicofKorea.vars
country_list.append(republicofKorea.vars)

southAfrica = TestDefaultSuite()
southAfrica.setup_method()
southAfrica.test_southAfrica()
southAfrica.teardown_method()
southAfrica.vars
country_list.append(southAfrica.vars)

singapore = TestDefaultSuite()
singapore.setup_method()
singapore.test_singapore()
singapore.teardown_method()
singapore.vars
country_list.append(singapore.vars)

slovakia = TestDefaultSuite()
slovakia.setup_method()
slovakia.test_slovakia()
slovakia.teardown_method()
slovakia.vars
country_list.append(slovakia.vars)

#sriLanka = TestDefaultSuite()
#sriLanka.setup_method()
#sriLanka.test_sriLanka()
#sriLanka.teardown_method()
#sriLanka.vars
#country_list.append(sriLanka.vars)

turkey = TestDefaultSuite()
turkey.setup_method()
turkey.test_turkey()
turkey.teardown_method()
turkey.vars
country_list.append(turkey.vars)

#test_unitedArabEmirates = TestDefaultSuite()
#test_unitedArabEmirates.setup_method()
#test_unitedArabEmirates.test_unitedArabEmirates()
#test_unitedArabEmirates.teardown_method()
#test_unitedArabEmirates.vars
#country_list.append(unitedArabEmirates.vars)

test_test_unitedKingdom = TestDefaultSuite()
test_test_unitedKingdom.setup_method()
test_test_unitedKingdom.test_unitedKingdom()
test_test_unitedKingdom.teardown_method()
test_test_unitedKingdom.vars
country_list.append(unitedKingdom.vars)

with open("list_data.txt", 'w', encoding="utf-8") as f:
                            for item in country_list:
                                f.write("%s\n" % item)
                            f.close()