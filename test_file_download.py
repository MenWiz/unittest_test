from util import *
import urllib.request

service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://the-internet.herokuapp.com/download')
link = driver.find_element(By.LINK_TEXT, 'doc1.txt')
destination = 'doc1'
url = link.get_attribute('href')
urllib.request.urlretrieve(url, destination)


class TestDownloadedFile(unittest.TestCase):

    """Checking file for word or sentence containing """

    def test_01_find_word_or_sentence(self):
        flag = True
        test_word_or_sentence = 'Action'   # defining desired word or sentence
        with open('doc1') as file:   # opening file for reading
            for line in file:
                if test_word_or_sentence in line:   # checking if desired word o sentence in line of text
                    flag = False
                    self.assertTrue(True)
                    break
            if flag:   # if desired word wasn't found fail testing and show message
                self.assertTrue(False, f'cannot find "{test_word_or_sentence}" word in text file')
