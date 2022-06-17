from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service)