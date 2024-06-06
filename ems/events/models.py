from django.db import models
from django.urls import reverse

class Event(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField(blank = True)
    venue = models.CharField()

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        """Get URL for event's detail view.

        Returns:
            str: URL for event detail.

        """
        return reverse("events:detail", kwargs={"pk": self.id})