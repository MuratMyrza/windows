from django.urls import path
from main.views import index, something


app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('something/', something)
]
