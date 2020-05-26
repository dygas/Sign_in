from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
def test_log_in():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('http://seleniumdemo.com/')
    driver.find_element(By.ID, 'menu-item-22').click()
    driver.find_element(By.ID, 'username').send_keys('slonko@pm.me')
    driver.find_element(By.ID, 'password').send_keys('testeroprogramowania')
    driver.find_element(By.ID, 'password').send_keys(Keys.ENTER)
