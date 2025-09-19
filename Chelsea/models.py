from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.title 
# Return first 50 characters of content for easy identification