import datetime
from django import forms
from todolist.models import Task
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.core import serializers
from django.urls import reverse
from datetime import date

class NewTodoForm(forms.Form):
    date = forms.DateField(label="Tanggal")
    title = forms.CharField(label="Judul")
    description = forms.CharField(
        label="Deskripsi", widget=forms.Textarea(attrs={"cols": ""})
    )

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todo_list = Task.objects.filter(user = request.user)
    user = request.user
    context = {
        'list_todo': todo_list,
        'username' : user,
    }
    return render(request, "todolist.html", context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user) # melakukan login terlebih dahulu
           return redirect("todolist:show_todolist")
        else:
            messages.info(request, 'Wrong Username or Password!')
    return render(request, 'login.html')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created successfully!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    return response

def create_task(request):
    if request.method == "POST":
        form = Form(request.POST)
        
        new_task = Task()
        new_task.user = request.user
        new_task.date = datetime.date.today()
        new_task.task_name = form.data['task_name']
        new_task.description = form.data['description']
        new_task.save()
        
        response = HttpResponseRedirect(reverse("todolist:show_todolist"))
        messages.success(request, 'Task saved.')
        return(response)
    else:
        context = {}
        return render(request, 'create_task.html', context)

def update_task(request, post_id: int):
    if request.method == "POST":
        task = Task.objects.filter(id=post_id, user=request.user).first()
        if task:
            task.is_finished = not task.is_finished
            task.save()
            messages.success(request, "Successful update!")
        else:
            messages.error(request, "Tasks not found!")

    return redirect("todolist:show_todolist")

def delete_task(request, post_id: int):
    if request.method == "POST":
        task = Task.objects.filter(id=post_id, user=request.user).first()
        if task:
            task.delete()
            messages.success(request, "Successfully deleted!")
        else:
            messages.error(request, "Tasks not found!")

    return redirect("todolist:show_todolist")

@login_required(login_url="/todolist/login")
def show_task_json(request: HttpRequest):
    todos = Task.objects.filter(user=request.user).order_by("date").all()
    return HttpResponse(
        serializers.serialize("json", todos), content_type="application/json"
    )


@login_required(login_url="/todolist/login")
def add_task_json(request: HttpRequest):
    if request.method == "POST":
        task = Task(
            date=date.fromisoformat(request.POST["date"]),
            title=request.POST["title"],
            description=request.POST["description"],
            user=request.user,
        )
        task.save()
        return HttpResponse(
            serializers.serialize("json", [task]),
            content_type="application/json",
        )
    return HttpResponse("Invalid method", status_code=405)


@login_required(login_url="/todolist/login")
def delete_task_json(request: HttpRequest, post_id: int):
    if request.method == "DELETE":
        task = Task.objects.filter(id=post_id, user=request.user).first()
        if task:
            task.delete()
            return HttpResponse("OK")
        else:
            return HttpResponse("Not Found", status_code=404)

    return HttpResponse("Invalid method", status_code=405)
