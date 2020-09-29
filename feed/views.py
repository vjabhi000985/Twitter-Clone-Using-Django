from django.shortcuts import render
from .models import tweets
# Create your views here.
def home(request):
    context = {'tweets': tweets.objects.all}
    return render(request,'feed/home.html',context)

