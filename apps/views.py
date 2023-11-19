from django.shortcuts import render, redirect
from .models import *
from .form import *

def index (request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    return render (request, 'htmls/list.html', {
        'tasks' : tasks,
        'form' : form,
    })

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method =='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render (request, 'htmls/update.html',{
        'form' : form
    }) 

def deleteTask (request, pk):
    item = Task.objects.get(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('/')

    return render (request, 'htmls/delete.html',{
        'item' : item
    })
