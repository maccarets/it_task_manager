from django import forms

from main_app.models import Task


class TaskForm(forms.ModelForm):
    # drivers = forms.ModelMultipleChoiceField(
    #     queryset=Driver.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )

    class Meta:
        model = Task
        fields = "__all__"
