from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class BasicInstallTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()
    
    def test_home_page_title(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Сайт Сергея Боталова', self.browser.title)

    def test_home_pahe_header(self):
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Serg Botalov', header.text)

    def test_home_page_blog(self):
        self.browser.get('http://127.0.0.1:8000')
        blog_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(blog_list)

    def test_home_page_articles_look_correct(self):
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(By.CLASS_NAME, 'article_title')
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article_summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

if __name__ == '__main__':
    unittest.main()