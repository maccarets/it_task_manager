from django.urls import path, include

from main_app.views import index, TasksListView, WorkersListView, TaskCreateView, WorkerCreateView, TaskTypeListView

urlpatterns = [
    path("", index, name="index"),
    path("tasks", TasksListView.as_view(), name="task-list"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path("tasks/types", TaskTypeListView.as_view(), name="task-types-list"),

    path("workers", WorkersListView.as_view(), name="worker-list"),
    path("registration", WorkerCreateView.as_view(), name="registration"),

]

app_name = "main_app"
