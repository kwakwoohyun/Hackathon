
from django.contrib import admin
from django.urls import path, include
import theme.views
import show.views
import fortune.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('theme.urls')),
    path('<int:show_id>/gallerydetail/', show.views.gallerydetail, name='gallerydetail'),
    path('lottery/',  fortune.views.lottery, name='lottery'),
    path('enroll/',  fortune.views.enroll, name='enroll'),
    path('send/',  fortune.views.sendEmail, name='send'),

]
