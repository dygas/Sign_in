import unittest
from selenium import webdriver
class MainTests(unittest.TestCase):
   def test_demo_login(self):
       driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
       driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
       title = driver.title
       print(title)
       assert 'Demobank - Bankowość Internetowa - Logowanie' == title
       driver.quit()