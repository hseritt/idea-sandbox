"""Views module for the tasks app."""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from tasks.models import Task
from tasks.forms import TaskForm


def index(request):
    
    task_list = Task.objects.all()

    if request.method == 'POST':
    	task_form = TaskForm(request.POST)
    	if task_form.is_valid():
    		task_form.save()
    		task_form = TaskForm()

    else:
    	task_form = TaskForm()

    return render(
        request,
        'tasks_index.html',
        {
            'task_form': task_form,
            'task_list' : task_list,
        }
    )


def delete(request, task_id):

    task = Task.objects.get(pk=task_id)
    task.delete()

    return HttpResponseRedirect('/')
