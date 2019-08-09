from django.shortcuts import get_object_or_404, render, redirect
from .models import Fortune,User

def lottery(request):
    fortune = Fortune.objects
    return render(request, 'lottery.html',{'fortune': fortune})

def enroll(request):
    
    user = User(fortune_id= 1, email = 'starpin1014@likelion.org')
    user.save()

    return redirect('lottery')
