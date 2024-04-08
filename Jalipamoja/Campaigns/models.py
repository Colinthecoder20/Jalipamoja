from django.conf import settings
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
    image = models.ImageField(blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Campaigns', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
