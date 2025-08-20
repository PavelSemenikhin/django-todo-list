from django import forms

from Todolist.models import Task, Tag


class TaskCreateUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "is_done", "tags")

    # Check that the deadline cannot be earlier than the task creation date
    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        created = self.instance.datetime
        if deadline and created and deadline < created:
            raise forms.ValidationError(
                "Deadline cannot be earlier than the creation date."
            )

        return deadline
