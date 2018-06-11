from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

'''
binary = FirefoxBinary('/usr/bin/firefox')
browser = webdriver.Firefox(firefox_binary=binary)
'''

driver = webdriver.Firefox(executable_path = '/usr/bin/geckodriver')
