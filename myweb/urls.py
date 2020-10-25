from django.urls import path
from django.contrib.auth import views as aunt_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logins', aunt_views.LoginView.as_view(template_name='myweb/logins.html'), name='logins'),
    path('logout', aunt_views.LogoutView.as_view(template_name='myweb/logins.html'), name='logout'),
    path('user', views.user, name= 'user'),
    path('home', views.home, name='home'),
    path('admins', views.admins, name= 'admins'),
    path('contact', views.contact, name= 'contact'),
    path('traveldo', views.traveldo, name= 'traveldo')


    
]