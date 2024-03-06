from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
    path('category/<slug:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<slug:slug>/', PostsByTag.as_view(), name='tag'),
]
