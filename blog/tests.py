from datetime import datetime
import pytz
from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.urls import resolve
from .views import home_page, article_page
from .models import Article


class ArticlePageTest(TestCase):
    
    def test_article_page_display_correct(self):
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summury 1',
            category='category 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug',
        )

        request = HttpRequest()
        response = article_page(request, 'slug')
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('full_text 1', html)        
        self.assertNotIn('summury 1', html)




class HomePageTest(TestCase):

    def test_home_page_displays_articles(self):
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summury 1',
            category='category 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1',
        )
        Article.objects.create(
            title='title 2',
            full_text='full_text 2',
            summary='summury 2',
            category='category 2',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-2',
        )

        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('full_text 1', html)        
        self.assertNotIn('summury 1', html)
        self.assertIn('blog/slug-1', html)  

        self.assertIn('title 2', html)
        self.assertIn('full_text 2', html)        
        self.assertNotIn('summury 2', html)
        self.assertIn('blog/slug-2', html)  

    def test_home_page_returns_correct_html(self):
        url = reverse('home_page')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/home_page.html')


class ArticleModelTest(TestCase):

    def test_article_model_save_and_retrive(self):
        article1 = Article(
            title='article 1',
            full_text='full_text 1',
            summary='summury 1',
            category='category 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1',
        )
        article1.save()

        article2 = Article(
            title='article 2',
            full_text='full_text 2',
            summary='summury 2',
            category='category 2',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-2',
        )
        article2.save()

        all_articles = Article.objects.all()

        self.assertEqual(len(all_articles), 2)
        self.assertEqual(
            all_articles[0].title,
            article1.title
        )
        self.assertEqual(
            all_articles[1].title,
            article2.title
        )
        self.assertEqual(
            all_articles[0].slug,
            article1.slug
        )
        self.assertEqual(
            all_articles[1].slug,
            article2.slug
        )