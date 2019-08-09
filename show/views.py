from django.shortcuts import render, get_object_or_404
from .models import Show
# Create your views here.


def gallerydetail(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    
    return render(request, 'gallerydetail.html', {'show':show})
