from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    category = models.CharField(max_length=100)
    cover_image = models.CharField(max_length=700)
    content = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

