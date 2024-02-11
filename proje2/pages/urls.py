from django.urls import path
from .views import AnasayfaView
from .views import BlogView

urlpatterns=[
    path('', AnasayfaView.as_view(),name='anasayfa'),
    path('blog/',BlogView.as_view(), name='blog')
    ]