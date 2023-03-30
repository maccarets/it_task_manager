from django import forms
from django.contrib.auth.forms import UserCreationForm

from main_app.models import Task, Worker, TaskType


class TaskForm(forms.ModelForm):
    # drivers = forms.ModelMultipleChoiceField(
    #     queryset=Driver.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )

    class Meta:
        model = Task
        fields = "__all__"


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = "__all__"


class WorkerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Worker
