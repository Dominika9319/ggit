"""goodmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from movies import views

from django.urls import include

urlpatterns = [
    path('', views.index, name="index"),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile_view, name='user_profile'),
    path('accounts/signup/', views.user_signup, name="user_signup"),
    path('log/', views.log),
    

    path('filmy/', views.movies_list),
    path('filmy/<int:movie_id>', views.movie_detail, name="movie_detail"),
    path('recenzje/', views.review_list, name="review_list"),
    path('director/', views.director),
    path('subpage/', views.subpage),
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),
    path('movies/', views.movies),
]

# http://127.0.0.1:8000/hello/
# http://127.0.0.1:8000/admin
# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/filmy
# http://127.0.0.1:8000/accounts/login/
# http://127.0.0.1:8000/accounts/signup
# http://127.0.0.1:8000/accounts/profile
# http://127.0.0.1:8000/log
# http://127.0.0.1:8000/recenzje
# http://127.0.0.1:8000/director
# http://127.0.0.1:8000/accounts/subpage

