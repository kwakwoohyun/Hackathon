from django.shortcuts import render
from .models import Show
# Create your views here.


def gallerydetail(request):
    show = Show.objects
    
    return render(request, 'gallerydetail.html', {'show':show})
