from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

class TaskList(ListView):
    model = Task
    template_name = 'template.html'
    context_object_name = 'tasks'

class TaskDetail(ListView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskCreate(ListView):
    model = Task
    fields = ['name', 'description', 'status', 'priority', 'progress_termin']
    template_name = 'task_create.html'
    context_object_name = 'task'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(ListView):
    model = Task
    fields = ['name', 'description', 'status', 'priority', 'progress_termin']
    template_name = 'task_update.html'
    context_object_name = 'task'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDelete(ListView):
    model = Task
    template_name = 'task_update.html'
    context_object_name = 'task'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
