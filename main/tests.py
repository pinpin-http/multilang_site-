from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Author

class AuthorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.author = Author.objects.create(user=self.user, name='Test Author')

    def test_author_creation(self):
        self.assertTrue(isinstance(self.author, Author))
        self.assertEqual(self.author.__str__(), self.author.name)

class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.author = Author.objects.create(user=self.user, name='Test Author')
        self.article = Article.objects.create(title='Test Article', content='Test Content', author=self.author)

    def test_article_creation(self):
        self.assertTrue(isinstance(self.article, Article))
        self.assertEqual(self.article.__str__(), self.article.title)

class AuthViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login(self):
        login = self.client.login(username='testuser', password='12345')
        self.assertTrue(login)

    def test_logout(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)  # Redirect after logout

class ArticleViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.author = Author.objects.create(user=self.user, name='Test Author')
        self.article = Article.objects.create(title='Test Article', content='Test Content', author=self.author)

    def test_article_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')

    def test_article_detail_view(self):
        response = self.client.get(f'/articles/{self.article.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')
