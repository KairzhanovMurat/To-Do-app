from django.shortcuts import render,redirect
from . models import Task
from .forms import TaskForm
from django.views.generic import ListView

# Create your views here.





def addTask(request):
    form = TaskForm()
    all_tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
        return redirect('/')
    context = {'form': form,
               'tasks' : all_tasks}
    search_input = request.GET.get('search') or ''
    context['search_input'] = search_input
    if search_input:
        context['tasks'] = Task.objects.filter(title__contains=search_input)

    return render(request,'Tasks.html',context=context)

def deleteTask(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')



