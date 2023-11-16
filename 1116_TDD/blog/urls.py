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
