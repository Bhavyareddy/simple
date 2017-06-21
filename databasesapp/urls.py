from django.conf.urls import url
from databasesapp import views
urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^save/', views.save, name='save'),
    url(r'^home1/', views.home1, name='home1'),
    url(r'^save1/', views.save1, name='save1'),

]