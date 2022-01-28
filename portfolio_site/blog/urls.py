#This file is where we will define our paths to our different webpages. This will be the urls for our views
#I.E if im on google, the path url for the settings is different than the path for the search, this page determines those paths
from django.urls import path
from . import views #Calls the views file

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]

#acess views then go to the index

