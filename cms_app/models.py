from django.db import models

# Create your models here.

class Expenses(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)
    # date = models.DateTimeField(auto_new_add=True)

    def __str__(self):
        return self.name
    