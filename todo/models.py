from django.db import models

# Create your models here.
class todos(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=500,blank=True)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
