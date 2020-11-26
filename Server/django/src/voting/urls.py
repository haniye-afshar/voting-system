"""voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import home_page,add_element,start_voting,reset,voting_page,login_page,register_page,logout_view,submit,update_score,result_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('addelement/', add_element ),
    path('start_voting/', start_voting ),
    path('reset/', reset ),
    path('voting/', voting_page ),
    path('voting/submit/', submit ),
    path('results/', result_page ),
    path('voting/update/', update_score ),
    path('login/',login_page),
    path('register/login/',login_page),
    path('register/',register_page),
    path('login/register/',register_page),
    path("logout/", logout_view)
]

