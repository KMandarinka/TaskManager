from django.urls import path
from . import views
#hjjhjj
urlpatterns = [
    path('', views.index, name = 'home'),
    path('about-us', views.about, name = 'about'),
    path('create', views.create, name = 'create'),
]
