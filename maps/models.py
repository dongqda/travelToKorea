from django.db import models

# Create your models here.
class DetailInform(models.Model) :
    title = models.CharField(max_length=100)
    image_lists = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title
    