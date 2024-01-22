from datetime import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from blog.models import Article
import unittest

class BasicInstallTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summury 1',
            category='category 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug',
        )

    def tearDown(self) -> None:
        self.browser.quit()
    
    def test_home_page_title(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Сайт Сергея Боталова', self.browser.title)

    def test_home_pahe_header(self):
        self.browser.get(self.live_server_url)
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Serg Botalov', header.text)

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        header = self.browser.find_element(By.TAG_NAME, 'h1')

        self.assertTrue(header.location['x'] > 10)

    def test_home_page_blog(self):
        self.browser.get(self.live_server_url)
        blog_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(blog_list)

    def test_home_page_articles_look_correct(self):
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, 'article_title')
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article_summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    def test_home_page_article_title_link_leads_to_page(self):
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, 'article_title')
        article_title_text = article_title.text
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        self.browser.get(article_link.get_attribute('href'))
        article_page_title = self.browser.find_element(By.CLASS_NAME, 'article_title')
        self.assertEqual(article_title_text, article_page_title.text)


