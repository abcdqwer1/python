from django.test import TestCase
from bs4 import BeautifulSoup
from .models import Post


class Test(TestCase):
    def setUp(self):
        print('-- blog app 테스트 시작 --')

    def test_main(self):
        print('-- / 테스트 --')

        print('-- 접속 확인 --')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'index')

        print('-- 상속 확인 --')
        header = soup.header
        self.assertIn('header', header.text)

        body = soup.body
        self.assertIn('index', body.text)

        footer = soup.footer
        self.assertIn('footer', footer.text)


    def test_about(self):
        print('-- about 테스트 --')

        print('-- 접속 확인 --')
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'about')

        print('-- 상속 확인 --')
        header = soup.header
        self.assertIn('header', header.text)

        body = soup.body
        self.assertIn('about', body.text)

        footer = soup.footer
        self.assertIn('footer', footer.text)


    def test_contact(self):
        print('-- contact 테스트 --')

        print('-- 접속 확인 --')
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'contact')

        print('-- 상속 확인 --')
        header = soup.header
        self.assertIn('header', header.text)

        body = soup.body
        self.assertIn('contact', body.text)

        footer = soup.footer
        self.assertIn('footer', footer.text)


    def test_post_list(self):

        post_test = Post.objects.create(
            title = '테스트를 위한 포스트',
            content = 'Hello World. We are the world.',
        )

        print('-- /blog 테스트 --')

        print('-- 접속 확인 --')
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'BLOG main')

        print('-- 상속 확인 --')

        header = soup.header
        self.assertIn('header', header.text)

        body = soup.body
        self.assertIn('post', body.text)

        footer = soup.footer
        self.assertIn('footer', footer.text)

        print('-- 포스트 목록 확인 --')
        print(dir(soup))
        if Post.objects.count() == 0:
            print('게시물이 없음')
            self.assertIn('게시물이 없습니다. 첫번째 게시물에 주인공이 되세요!', soup.body.text)
        else:
            print('게시물이 있음')
            print(Post.objects.count())
            print(len(soup.body.select('h2')))
            self.assertGreater(len(soup.body.select('h2')), 0)


    def test_post_detail(self):
        print('-- post_detail 테스트 --')

        print('-- 접속 확인 --')
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'post_detail')

        print('-- 상속 확인 --')

        header = soup.header
        self.assertIn('header', header.text)
        footer = soup.footer
        self.assertIn('footer', footer.text)

        print('-- 제목 확인 --')
        print(dir(soup))

        self.assertIn('', soup.body.text)
        self.assertIn('', soup.body.text)
        self.assertIn('', soup.body.text)
