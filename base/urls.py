from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('l/<str:uri>', views.redirector, name='redirector')
]