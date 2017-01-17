from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

import unittest
import time
import random


class LabsterTest(unittest.TestCase):
    BASE_URL = 'https://staging-courses.labster.com/'
    REGISTER_URL = BASE_URL + 'register?next=/dashboard'
    PROFILE_URL = BASE_URL + 'account/settings'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_register_and_update_profile(self):
        self.driver.get(self.REGISTER_URL)

        random_number = random.randint(0, 1000)

        self.driver.find_element_by_id(
            'register-email').send_keys('test_{}@test.com'.format(random_number))

        name = 'Test {}'.format(random_number)
        self.driver.find_element_by_id('register-name').send_keys(name)

        username = 'test_{}'.format(random_number)
        self.driver.find_element_by_id('register-username').send_keys(username)

        self.driver.find_element_by_id(
            'register-password').send_keys('testtest')

        gender_box = self.driver.find_element_by_id('register-gender')
        options = gender_box.find_elements_by_tag_name('option')

        select = Select(gender_box)
        select.select_by_value(options[1].get_attribute('value'))

        birth_box = self.driver.find_element_by_id('register-year_of_birth')
        options = birth_box.find_elements_by_tag_name('option')

        select = Select(birth_box)
        select.select_by_value(options[3].get_attribute('value'))

        education_box = self.driver.find_element_by_id(
            'register-level_of_education')
        options = education_box.find_elements_by_tag_name('option')

        select = Select(education_box)
        select.select_by_value(options[3].get_attribute('value'))

        self.driver.find_element_by_id('register-honor_code').click()

        self.driver.find_element_by_xpath(
            '//button[text()="Create your account"]').click()

        time.sleep(5)

        self.driver.get(self.PROFILE_URL)
        time.sleep(4)

        name = name + ' Edit'
        self.driver.find_element_by_id('u-field-input-name').clear()

        self.driver.find_element_by_id('u-field-input-name').send_keys(name)
        self.driver.find_element_by_id('u-field-input-email').click()

        time.sleep(2)
        self.driver.get(self.PROFILE_URL)

        time.sleep(3)
        updated_name = self.driver.find_element_by_id(
            'u-field-input-name').get_attribute('value')

        self.assertEqual(name, updated_name)


if __name__ == '__main__':
    unittest.main()
