from django.urls import path
from .views import homeview

app_name = 'core'
urlpatterns = [
    path('', homeview, name="home_page"),
]