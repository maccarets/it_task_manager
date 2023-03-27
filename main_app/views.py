from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from main_app.forms import TaskForm
from main_app.models import Task, Worker


def index(request):
    return render(request, "main_app/index.html")


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "main_app/task_form.html"
    success_url = reverse_lazy("main_app:task-list")


class WorkersListView(LoginRequiredMixin, generic.ListView):
    model = Worker
