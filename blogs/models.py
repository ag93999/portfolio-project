from django.db import models


class Blog(models.Model):
    """
    This model keeps a record of all the blog details.
    """
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:60]

    def display_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
