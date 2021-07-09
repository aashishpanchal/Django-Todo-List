from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import TODOModel
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    user = request.user.is_anonymous
    todo = None
    if not(user):
        name = str(request.user)
        todo = TODOModel.objects.filter(user=request.user)
    
    context = {"userLogin": not(user), "data":todo}
    return render(request, 'index.html', context=context)

def Singin(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            messages.success(request, "Successfully create your Account.!")

        return render(request, 'Signin.html')
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    

def Login(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.warning(request, "wrong information.!")
    return render(request, 'Login.html')

@login_required
def Logout(request):
    logout(request)
    return redirect("/Login/")

def About(request):
    todo = TODOModel.objects.filter(user=request.user)
    return render(request, 'About.html', context={"data": todo})

@login_required
def Create(request):
    if request.method == 'POST':
        title = request.POST.get("Title")
        content = request.POST.get("Content")
        important = bool(request.POST.get("Important", False))
        name = str(request.user)

        todo = TODOModel(Title=title, Description=content, Important=important, user=request.user)
        todo.save()
        messages.success(request, 'Your TODO is Save.!')
    return render(request, 'Create.html')

@login_required
def Update(request, pk, n):
    todo = TODOModel.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get("Title")
        content = request.POST.get("Content")
        important = bool(request.POST.get("Important", False))
        todo.Title = title
        todo.Description = content
        todo.Important = important
        todo.DateTime = timezone.now()
        todo.save()

        messages.success(request, 'Your TODO is Update.!')
    return render(request, 'Update.html', context={"data": todo})

@login_required
def Delete(request, pk, n):
    todo = TODOModel.objects.get(pk=pk)
    todo.delete()
    messages.success(request, f'TODO Nummber {n} is Deleted.!')
    return redirect('/')
    