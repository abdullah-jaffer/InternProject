from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_article/', views.get_news, name='get_news'),
    path('post_article/', views.post_news, name='post_news')
]
