from django.db import models


# Create your models here.
class Todolists(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=5000)
    status = models.CharField(default='Awaiting', max_length=15)
    due = models.DateField()

    def __str__(self):
        return self.title
