from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from main_app.forms import TaskForm, WorkerCreationForm, TaskTypeForm
from main_app.models import Task, Worker, TaskType


def index(request):
    context = {}

    return render(request, "main_app/index.html")


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "main_app/task_form.html"
    success_url = reverse_lazy("main_app:task-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "main_app/task_type_list.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "main_app/task_type_form.html"
    success_url = reverse_lazy("main_app:task-type-list")




class WorkersListView(LoginRequiredMixin, generic.ListView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("main_app:index")