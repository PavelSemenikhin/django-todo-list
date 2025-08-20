from django.urls import path
from Todolist.views import (
    HomeView,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    TaskUpdateView,
    TaskDeleteView,
    task_toggle_status_view,
    TaskCreateView
)

app_name = "todolist"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/toggle/",
        task_toggle_status_view,
        name="task-toggle"
    ),
]
