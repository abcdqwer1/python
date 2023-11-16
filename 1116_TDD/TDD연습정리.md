python -m venv venv

pip install django

django-admin startproject tdd .

python .\manage.py startapp blog

------------------------------------------------------------------------------
# tdd > settings.py

## 호스트 전체허용
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
## blog 추가
    'blog',
]

TEMPLATES = [
    {
## BASE_DIR / 'templates' 추가
        'DIRS': [BASE_DIR / 'templates'], 
    }
]

# 언어변경
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'

------------------------------------------------------------------------------
# tdd > urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

------------------------------------------------------------------------------
# blog > models.py
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

------------------------------------------------------------------------------
# migrate
python .\manage.py makemigrations
python .\manage.py migrate

------------------------------------------------------------------------------
# blog > urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.post_list, name='post_list'),
    # path('blog/new/', views.post_new, name='post_new'),
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
]

------------------------------------------------------------------------------
# blog > views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from .models import Post

class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
index = IndexView.as_view()

class AboutView(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
about = AboutView.as_view()

class ContactView(TemplateView):
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
contact = ContactView.as_view()

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post 
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.save()
        return super().get_object(queryset)

post_detail = PostDetailView.as_view()

------------------------------------------------------------------------------
# templates > blog > post_list.html

<!DOCTYPE html>
<html lang="ko-KR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BLOG main</title>
</head>

<body>
    <header>post_list header</header>

    {% if post_list.exists %}
    {% for post in object_list %}
            <section class="body">
                <h2 class='contents-heading'>{{ post.title }}</h2>
                <p class='contents-text'>{{ post.content }}</p>
                <p class='contents-updated' style="font-size: small;">최종 수정 날짜: {{ post.updated_at }}</p>
                <a class="btn" href="{% url 'blog:post_detail' post.pk %}">자세히</a>
                <br><br><br><br>
            </section>
    {% endfor %}
    {% else %}
    <p>게시물이 없습니다. 첫번째 게시물에 주인공이 되세요!</p>
    {% endif %}

    <footer>post_list footer</footer>
</body>
</html>

------------------------------------------------------------------------------
#  templates > blog > post_detail.html

<!DOCTYPE html>
<html lang="ko-KR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>post_detail</title>
</head>

<body>
    <header>post_detail header</header>

    <section class='contents-section'>
        <h2 class='contents-heading'>{{ post.title }}</h2>
        <p class='contents-text'>{{ post.content }}</p>
        <p class='contents-updated'>최종 수정 날짜: {{ post.updated_at }}</p>
    </section>

    <footer>post_detail footer</footer>
</body>
</html>
------------------------------------------------------------------------------
# templates > blog > index.html
# 똑같이 about, contact 작성

<!DOCTYPE html>
<html lang="ko-KR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index</title>
</head>

<body>
    <header>index header</header>
    index
    <footer>index footer</footer>
</body>
</html>

------------------------------------------------------------------------------
# blog > tests.py

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







'ASCII_SPACES', 'DEFAULT_BUILDER_FEATURES', 'DEFAULT_INTERESTING_STRING_TYPES', 'EMPTY_ELEMENT_EVENT', 'END_ELEMENT_EVENT', 'NO_PARSER_SPECIFIED_WARNING', 'ROOT_TAG_NAME', 'START_ELEMENT_EVENT', 'STRING_ELEMENT_EVENT', '__bool__', '__call__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', 
'__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_all_strings', '_clone', '_decode_markup', '_event_stream', '_feed', '_find_all', '_find_one', '_format_tag', '_indent_string', '_is_xml', '_lastRecursiveChild', '_last_descendant', '_linkage_fixer', '_markup_is_url', '_markup_resembles_filename', '_most_recent_element', 
'_namespaces', '_popToTag', '_should_pretty_print', 'append', 'attrs', 'builder', 'can_be_empty_element', 'cdata_list_attributes', 'childGenerator', 'children', 'clear', 'contains_replacement_characters', 'contents', 'css', 'currentTag', 'current_data', 'declared_html_encoding', 'decode', 'decode_contents', 'decompose', 'decomposed', 'default', 'descendants', 'element_classes', 'encode', 'encode_contents', 'endData', 'extend', 'extract', 'fetchNextSiblings', 'fetchParents', 'fetchPrevious', 'fetchPreviousSiblings', 'find', 'findAll', 'findAllNext', 'findAllPrevious', 'findChild', 'findChildren', 'findNext', 'findNextSibling', 'findNextSiblings', 'findParent', 'findParents', 'findPrevious', 'findPreviousSibling', 'findPreviousSiblings', 'find_all', 'find_all_next', 'find_all_previous', 'find_next', 'find_next_sibling', 'find_next_siblings', 'find_parent', 'find_parents', 'find_previous', 'find_previous_sibling', 'find_previous_siblings', 'format_string', 'formatter_for_name', 'get', 'getText', 'get_attribute_list', 'get_text', 'handle_data', 'handle_endtag', 'handle_starttag', 'has_attr', 'has_key', 'hidden', 'index', 'insert', 'insert_after', 'insert_before', 'interesting_string_types', 'isSelfClosing', 'is_empty_element', 'is_xml', 'known_xml', 'markup', 'name', 'namespace', 'new_string', 'new_tag', 'next', 'nextGenerator', 'nextSibling', 'nextSiblingGenerator', 'next_element', 'next_elements', 'next_sibling', 'next_siblings', 'object_was_parsed', 'open_tag_counter', 'original_encoding', 'parent', 'parentGenerator', 'parents', 'parse_only', 'parserClass', 'parser_class', 'popTag', 'prefix', 'preserve_whitespace_tag_stack', 'preserve_whitespace_tags', 'prettify', 'previous', 'previousGenerator', 'previousSibling', 'previousSiblingGenerator', 'previous_element', 'previous_elements', 'previous_sibling', 'previous_siblings', 'pushTag', 'recursiveChildGenerator', 'renderContents', 'replaceWith', 'replaceWithChildren', 'replace_with', 'replace_with_children', 'reset', 'select', 'select_one', 'self_and_descendants', 'setup', 'smooth', 'string', 'string_container', 'string_container_stack', 'strings', 'stripped_strings', 'tagStack', 'text', 'unwrap', 'wrap'
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
