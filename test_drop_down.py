from util import *
from selenium.webdriver.support.ui import Select

service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service)


class DropDownTest(unittest.TestCase):

    """Testing dropdown menu working properly"""

    driver.get('https://the-internet.herokuapp.com/dropdown')
    drop = Select(driver.find_element(By.ID, 'dropdown'))

    def test_01_values_selected(self):

        """Testing that dropdown option definitely selected, when was selected in UI"""

        for i in range(1, len(self.drop.options)):   # Using iteration in case here will be more options in future
            self.drop.select_by_index(i)
            self.assertTrue(driver.find_element(By.XPATH, f'//*[@id="dropdown"]/option[{i + 1}]').is_selected())

    def test_02_dropdown_options_name(self):

        """ Testing that selected dropdown option has a correct name """

        for i in range(1, len(self.drop.options)):   # Using iteration in case here will be more options in future
            self.drop.select_by_index(i)
            self.assertTrue(driver.find_element(By.XPATH, f'//*[@id="dropdown"]/option[{i + 1}]').text == f'Option {i}')
