from util import *

service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service)


class TestKeyPresses(unittest.TestCase):   # class for testing Key pressing functionality

    driver.get("https://the-internet.herokuapp.com/key_presses")
    text = driver.find_element(By.ID, 'target')   # Locating text input field in DOM
    result = driver.find_element(By.ID, 'result').text   # Locating element with text output result

    def test_01_a_to_z(self):   # Testing all literal symbols from 'a' to 'z'
        self.text.clear()
        for i in range(97, 123):   # using ASCII table to find and test necessary symbols
            self.text.send_keys(chr(i))
            self.assertEqual(driver.find_element(By.ID,'result').text, f"You entered: {chr(i)}")

    def test_02_symbols(self):   # Testing not literal symbols like '/', '#' and etc.
        self.text.clear()
        symbols = []
        symbols.extend(range(33, 48))   # extend our list with different symbols from ASCII table
        symbols.extend(range(58, 65))
        symbols.extend(range(91, 97))
        symbols.extend(range(123, 126))
        for elem in symbols:
            self.text.send_keys(chr(elem))
            self.assertEqual(driver.find_element(By.ID,'result').text, f"You entered: {chr(elem)}")

    def test_03_A_to_Z(self):   # Testing all capital literal symbols from 'A' to 'Z'
        self.text.clear()
        for i in range(65, 91):   # using ASCII table to find and test necessary symbols
            self.text.send_keys(chr(i))
            self.assertEqual(driver.find_element(By.ID, 'result').text, f"You entered: {chr(i)}")

    def test_04_numbers(self):   # Testing all the numbers from '0' to '9'
        self.text.clear()
        for i in range(48, 58):   # using ASCII table to find and test necessary numbers
            self.text.send_keys(chr(i))
            self.assertEqual(driver.find_element(By.ID, 'result').text, f"You entered: {chr(i)}")

    def test_05_commands(self):   # Testing command buttons on keyboard
        self.text.clear()
        self.text.send_keys(webdriver.Keys.CONTROL)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: CONTROL')
        self.text.send_keys(webdriver.Keys.SHIFT)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: SHIFT')
        self.text.send_keys(webdriver.Keys.DELETE)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: DELETE')
        self.text.send_keys(webdriver.Keys.ALT)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: ALT')
        self.text.send_keys(webdriver.Keys.ESCAPE)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: ESCAPE')
        self.text.send_keys(webdriver.Keys.BACKSPACE)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: BACK_SPACE')

    def test_06_f1_f12(self):   # Testing F1 - F12 buttons pressing
        self.text.send_keys(webdriver.Keys.F1)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F1')
        self.text.send_keys(webdriver.Keys.F2)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F2')
        self.text.send_keys(webdriver.Keys.F3)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F3')
        self.text.send_keys(webdriver.Keys.F4)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F4')
        self.text.send_keys(webdriver.Keys.F5)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F5')
        self.text.send_keys(webdriver.Keys.F6)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F6')
        self.text.send_keys(webdriver.Keys.F7)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F7')
        self.text.send_keys(webdriver.Keys.F8)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F8')
        self.text.send_keys(webdriver.Keys.F9)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F9')
        self.text.send_keys(webdriver.Keys.F10)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F10')
        self.text.send_keys(webdriver.Keys.F11)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F11')
        self.text.send_keys(webdriver.Keys.F12)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: F12')

    def test_07_enter(self):   # Testing ENTER button
        self.text.clear()
        self.text.send_keys(webdriver.Keys.ENTER)
        self.assertEqual(driver.find_element(By.ID, 'result').text, 'You entered: ENTER')
