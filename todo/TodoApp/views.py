from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from TodoApp.models import Todo
from django.contrib.auth import authenticate, login as LoginUser, logout as logoutUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from TodoApp.forms import TodoForm
from django.db.models import Q
from django.views.generic.edit import UpdateView


def index(request):
    if request.user.is_authenticated:
        taskss(request)
        return redirect('task')
    else:
        return render(request,'index.html')

@login_required(login_url='login')
def taskss(request):
    if request.user.is_authenticated:
        usern = request.user
        todos = Todo.objects.filter(user=usern)
        counts = Todo.objects.filter(user=usern).filter(status="P").count()
        form = TodoForm()
        return render(request, "Home.html", context={'form' : form, 'todos' : todos, 'counts' : counts})
  
     

@login_required(login_url='login')
def addtodo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("task")
        else: 
            return render(request , 'Home.html' , context={'form' : form})

@login_required(login_url='login')
def deletetodo(request, id):
    Todo.objects.get(pk = id).delete()
    return redirect('task')
    

@login_required(login_url='login')
def changestatus(request, id, status ):
    todo = Todo.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('task')

@login_required(login_url='login')
def updatetodo(request,id):
    todo = Todo.objects.get(pk = id)
    ti = todo.title
    print(todo)
    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.desc = request.POST.get("desc")
        # print(title,desc)
        todo.save()
        return redirect('task')
    
    return render(request,"update.html", context={'ti' : ti})


# class Updatetodo(LoginRequiredMixin,UpdateView):
#     model = Todo
#     fields = ['title', 'desc']
#     template_name = "update.html"
#     success_url = reverse_lazy('task')


def login(request):
    context = {
        "alert" : "Invalid Username or password"
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                LoginUser(request,user)
                return HttpResponseRedirect(reverse('task'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', {})



    
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'register.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'register.html' , context=context)

@login_required(login_url='login')
def signout(request):
    logoutUser(request)
    return redirect('login')

def about(request):
    return render(request, "About.html")


@login_required(login_url='login')
def searchtodo(request):
    if request.user.is_authenticated:
        usern = request.user
        search_input = request.GET.get('search') or ''
        print(search_input)
        results = Todo.objects.filter(user=usern).filter(Q(title__icontains=search_input) | Q(desc__icontains=search_input))
        return render(request , 'Home.html', context={'todos' : results} )