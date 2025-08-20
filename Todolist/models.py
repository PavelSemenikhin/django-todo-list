from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["is_done", "-datetime"]

    def __str__(self):
        return self.content
