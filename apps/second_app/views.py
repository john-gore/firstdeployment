from django.shortcuts import render, redirect
def index(request):
    # need to set the html page to success
    return render(request, "second_app/index.html")
# Create your views here.
