from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import users
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "indexfirst.html")
def register(request):
    result = users.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!!")
    print request.POST['first_name']
    print request.POST['last_name']
    print request.POST['email']
    print request.POST['password']
    users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'] )
    print users.objects.all()
    return redirect("/success")

def login(request):
    result = users.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': users.objects.get(id=request.session['user_id'])
    }
    return render(request, 'indexsecond.html', context)
