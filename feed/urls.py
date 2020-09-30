from django.urls import path
from . import views
from .views import TweetListView,TweetCreateView,TweetUpdateView,TweetDeleteView
urlpatterns = [
    path('',TweetListView.as_view(),name='home'),
    path('create/',TweetCreateView.as_view(),name='tweetcreate'),
    path('tweets/<int:pk>/update',TweetUpdateView.as_view(),name='tweetupdate'),
    path('tweets/<int:pk>/delete',TweetDeleteView.as_view(),name='tweetdelete'),

]