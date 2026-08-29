from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TaskForm
from .models import Task
from .mixins import UserIsOwnerMixin

class TaskList(ListView):
    model = Task
    template_name = 'template.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'
    context_object_name = 'task'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    context_object_name = 'task'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDelete(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    template_name = 'task_update.html'
    context_object_name = 'task'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
