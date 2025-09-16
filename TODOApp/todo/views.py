from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title:  # simple validation
            Task.objects.create(title=title, description=description)
            return redirect('todo:task_list')
        error = "Title is required."
        return render(request, 'todo/task_form.html', {'error': error, 'title_text': '', 'desc_text': description})
    return render(request, 'todo/task_form.html', {'title_text': '', 'desc_text': ''})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        completed = request.POST.get('completed') == 'on'
        if title:
            task.title = title
            task.description = description
            task.completed = completed
            task.save()
            return redirect('todo:task_list')
        error = "Title is required."
        return render(request, 'todo/task_form.html', {
            'task': task, 'error': error,
            'title_text': title, 'desc_text': description, 'completed': completed
        })
    return render(request, 'todo/task_form.html', {
        'task': task,
        'title_text': task.title,
        'desc_text': task.description,
        'completed': task.completed
    })

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todo:task_list')
    return render(request, 'todo/confirm_delete.html', {'task': task})

def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect('todo:task_list')
