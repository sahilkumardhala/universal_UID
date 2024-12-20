"""
URL configuration for universal_UID project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from UIDapp import views
urlpatterns = [
    # path('UID/', include("UIDapp.urls")),
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('set_password/', views.set_password, name="set_password"),
    path('login/', views.login , name='login'),
    path('logout/', views.logout , name='logout'),
    path('User_dashboard/', views.User_dashboard ,name='User_dashboard'),
    path('admin/', admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
