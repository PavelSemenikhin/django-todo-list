from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from Todolist.forms import TaskCreateUpdateForm
from Todolist.models import Tag, Task


class HomeView(generic.ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "tasks"
    paginate_by = 10


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    paginate_by = 10
    template_name = "tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tag_form.html"
    success_url = reverse_lazy("todolist:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tag_confirm_delete.html"
    success_url = reverse_lazy("todolist:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)
    template_name = "tag_form.html"
    success_url = reverse_lazy("todolist:tag-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateUpdateForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todolist:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("todolist:home")


def task_toggle_status_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todolist:home")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateUpdateForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todolist:home")
