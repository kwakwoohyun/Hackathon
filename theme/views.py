from django.shortcuts import render
from django.views.generic. base import TemplateView
from show.models import Show

# Create your views here.
<<<<<<< HEAD
def MainpageView(request):
    show = Show.objects.all()
    return render(request,'index.html',{'show':show})

msg_plain = render_to_string('email.txt')
msg_html = render_to_string('email.html')

''' send_mail(
    '🥠포춘 티켓 응모 결과',
    msg_plain,
    settings.EMAIL_HOST_USER,
    ['starpin1014@likelion.org'],
    html_message=msg_html,
    fail_silently=False
) '''
=======

def MainpageView(request):
    show = Show.objects.all()
    return render(request,'index.html',{'show':show})
>>>>>>> 1230a10ab1f50034f70a0d86a306252d552edd35
