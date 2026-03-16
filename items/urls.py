from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('lostitems/', views.lostitems, name='lostitems'),
    path('founditems/', views.founditems, name='founditems')
]