from django.shortcuts import get_object_or_404, render, redirect
from .models import Fortune,User

def lottery(request):
    fortune = Fortune.objects
    return render(request, 'lottery.html',{'fortune': fortune})

def enroll(request):
    email = request.GET.get('email')
    user = User(fortune_id= 1, email = email)
    user.save()

    return redirect('lottery')
