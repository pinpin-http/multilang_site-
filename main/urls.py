from django.urls import path
from .views import article_list, article_detail, auth_view, logout_view, add_article
urlpatterns = [
    path('', article_list, name='article_list'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('auth/', auth_view, name='auth_view'),
    path('logout/', logout_view, name='logout'),
       path('add_article/', add_article, name='add_article'),
    ]


