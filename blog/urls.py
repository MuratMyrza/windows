from django.urls import path
from blog.views import add_post, add_theme, home, post, theme, search_result

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('post-<int:pk>/', post, name="post"),
    path('theme-<int:pk>/', theme, name="theme"),

    path('search-result/', search_result, name='search-result'),

    path('add/', add_post, name="add"),
    path('add_theme', add_theme, name='add_theme')
]
