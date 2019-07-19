from django.shortcuts import render
from django.views.generic. base import TemplateView

# Create your views here.
class MainpageView(TemplateView):
    template_name = 'index.html'
    
def gallerydetail(request):
    return render(request, 'gallerydetail.html')

def lottery(request):
    return render(request, 'lottery.html')