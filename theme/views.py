from django.shortcuts import render
from django.views.generic. base import TemplateView
from show.models import Show

# Create your views here.

def MainpageView(request):
    show = Show.objects.all()
    return render(request,'index.html',{'show':show})
