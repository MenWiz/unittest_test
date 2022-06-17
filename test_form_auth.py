from util import *

service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service)


class TestFormAuth(unittest.TestCase):

    driver.get("https://the-internet.herokuapp.com/login")

    def test_01_check_right_cred(self):

        """ Case for testing login with a right credential and then testing logout button """

        driver.find_element(By.NAME, 'username').send_keys('tomsmith')   # Testing right Login and Password
        driver.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
        driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
        self.assertTrue(' Secure Area' in driver.page_source)
        driver.find_element(By.XPATH, '//*[@id="content"]/div/a').click()  # Testing logout button
        self.assertEqual(driver.current_url, 'https://the-internet.herokuapp.com/login')

    def test_02_wrong_cred(self):

        """ Case for testing 3 different type of wrong auth """

        driver.find_element(By.NAME, 'username').send_keys('tommy')   # Login and Password wrong
        driver.find_element(By.NAME, 'password').send_keys('MegaPassBro!')
        driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
        self.assertEqual(driver.current_url, 'https://the-internet.herokuapp.com/login')

        driver.find_element(By.NAME, 'username').send_keys('Jimmy')   # Login wrong, Password empty
        driver.find_element(By.NAME, 'password').send_keys('')
        driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
        self.assertEqual(driver.current_url, 'https://the-internet.herokuapp.com/login')

        driver.find_element(By.NAME, 'username').send_keys('')   # Login empty, Password wrong
        driver.find_element(By.NAME, 'password').send_keys('Password')
        driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
        self.assertEqual(driver.current_url, 'https://the-internet.herokuapp.com/login')