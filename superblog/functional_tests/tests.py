from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os, unittest

class BlogTests (LiveServerTestCase):
       def setUp(self):
           self.browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

       def tearDown (self):
            self.browser.quit()

       # Insert our user story here

       def test_user_lands_on_home_page (self) :
              # John hears about a cool new blog and goes to check it out
              self.browser.get('http://localhost:8000')
              # John notices the blog title
              self.assertIn("Mark's blog",self.browser.title)
              # finish the test ...
           
        
