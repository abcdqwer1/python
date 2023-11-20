from django.urls import include, path
# from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register('post', views.PostViewSet) 

urlpatterns = [
    path('post/', views.post_list),
    path('post/<int:pk>/', views.post_detail), 
    path('post/new/', views.post_new), 
    # path('', include(router.urls)),
]