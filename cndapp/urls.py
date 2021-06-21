from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cnd_app, name='cnd_app'),
]
