from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self): 
        return  self.name
    
class Campaign(models.Model):
    category = models.ForeignKey(Category, related_name='Campaigns', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)   
    description = models.TextField(blank=True, null=True)
    amount = models.FloatField()
    image = models.ImageField(upload_to='Campaign_images', blank=False, null=False)
    is_closed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='Campaigns', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
