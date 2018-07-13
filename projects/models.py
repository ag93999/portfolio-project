from django.db import models


class project(models.Model):
    """
    This model keeps a record of all the project details.
    """
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=250)

    def __str__(self):
        return self.title
