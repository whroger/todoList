# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Todo
from django.http import Http404
from django.http import HttpResponse
from datetime import datetime, date
from django.utils.timezone import get_current_timezone


# Create your views here.
def index(request):
    todos = Todo.objects.filter(finished=False)
    finishedtodos = Todo.objects.filter(finished=True)
    context = {
        'todos' : todos,
        'finishedtodos' : finishedtodos,
    }
    #return HttpResponse('Hello World')
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo,
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        priority = request.POST['priority']
        deadlinea = request.POST['deadlinea']
        #deadline = datetime.strftime(deadlinea,'d%/m%/Y%')
        todo = Todo(title=title, text=text, priority=priority, deadline=deadlinea)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')

def edit(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo,
    }
    if(request.method == 'POST'):
        todo = Todo.objects.get(id=id)
        text = request.POST['text']
        priority = request.POST['priority']
        todo = Todo.objects.filter(id=id).update(text=text, priority=priority)
        return redirect('/todos')
    else:
        return render(request, 'edit.html', context)


def delete(request, id):
    try:todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
    return redirect('/todos')

def finished(request, id):
    try: todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        if todo.finished == False:
            todo = Todo.objects.filter(id=id).update(finished=True, finished_at=datetime.now())
        else:
            todo = Todo.objects.filter(id=id).update(finished=False)
    return redirect('/todos')