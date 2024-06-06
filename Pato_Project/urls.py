"""
URL configuration for Pato_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pato_Project import settings
from django.conf.urls.static import static
from main.views import IndexView, menu, about, ReservationView
from account.views import RegisterView, MyLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('menu/', menu, name='menu'),
    path('about/', about, name='about'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)