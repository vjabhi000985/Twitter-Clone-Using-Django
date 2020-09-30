from django.shortcuts import render
from .models import tweets
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.
class TweetListView(LoginRequiredMixin,ListView):
	model = tweets
	template_name = 'feed/home.html'
	ordering = ['-datetime']

class TweetCreateView(LoginRequiredMixin,CreateView):
	model = tweets
	template_name = 'feed/tweet_form.html'
	fields = ['text']
	success_url = '/'

	def form_valid(self,form):
		form.instance.uname = self.request.user
		return super().form_valid(form)

class TweetUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = tweets
	template_name = 'feed/tweet_form.html'
	fields = ['text']
	success_url = '/'

	def form_valid(self,form):
		form.instance.uname = self.request.user
		return super().form_valid(form)

	def test_func(self):
		tweets = self.get_object()
		if(self.request.user==tweets.uname):
			return True
		return False

class TweetDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = tweets
	template_name = 'feed/tweet_confirm_delete.html'
	success_url = '/'

	def test_func(self):
		tweets = self.get_object()
		if(self.request.user==tweets.uname):
			return True
		return False

