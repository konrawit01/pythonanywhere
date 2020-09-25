from django.contrib import admin
from django.urls import path, include
from myweb import views

urlpatterns = [
    path('', views.index),
    #path('polls/', include('polls.urls')),
    path('myweb/', include('myweb.urls')),
    path('united', views.united),
    path('admin/', admin.site.urls),
    path('login/', views.login,name="login"),
]
