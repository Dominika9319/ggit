from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

import datetime

def hello_world(request):
    my_context = {"time": datetime.datetime.now()}
    return render(request, template_name="hello.html", context=my_context)

from movies.models import Movie

def movies(request):
    my_context = {"movies": Movie.objects.all()}
    return render(request, template_name="movies.html", context=my_context)

def index(request):
    return render(request, template_name="index.html")

def subpage(request):
    return render(request, template_name="subpage.html")

from movies.models import Movie

def movies_list(request):
    my_context = {"movies": Movie.objects.all()}
    return render(request, template_name="movie_list.html", context=my_context)

def profile_view(request):
    return render(request, template_name="my_profile.html")



from django.contrib.auth.forms import UserCreationForm

def user_signup(request):
    if request.method == "POST":
        # przetwarzanie danych z formualrza
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name="registration/signup_complete.html")
    else:
        # czysty formularz do wypelnienia
        form = UserCreationForm()

    return render(
        request,
        template_name="registration/signup_form.html",
        context={'form':form}
    )

def password_reset(request):
    return render(request, template_name="password_reset_form.html")



def movie_detail(request, movie_id):
    my_context = {"movie": Movie.objects.get(id=movie_id)}
    return render(request, template_name="movie_detail.html", context=my_context)

from movies.models import Review

def review_list(request):
    my_context = {"reviews": Review.objects.all()}
    return render(request, template_name="review_list.html", context=my_context)


from movies.models import Director

def director(request):
    my_context = {"directors": Director.objects.all()}
    return render(request, template_name="director.html", context=my_context)



