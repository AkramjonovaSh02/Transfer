from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('tryouts/', Tryouts.as_view, name='tryouts' ),
    path('about/', About.as_view, name='about')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
