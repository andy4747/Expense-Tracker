from django.db import models

# Create your models here.

class Expenses(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)
    # date = models.DateTimeField(auto_new_add=True)

    def __str__(self):
        return self.name
    
class AppUsers(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    # password = models.CharField(max_length=32, widget=forms.PasswordInput)