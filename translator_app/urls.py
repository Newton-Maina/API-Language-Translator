from django.urls import path
from . import views

app_name = 'translator_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('translator/', views.translator, name='translator'),
    path('translation/', views.translation, name='translation'),
]