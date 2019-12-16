from django.db import models
from dictionary.models import Category

class Firm(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='user_img')
    
    def __str__(self):
	    return "%s" %self.name
        
    # @property
    # def category(self):
    #     q = Category.objects.filter(instruments_of_category__firm=self).distinct()
    #     return q
        
    class Meta:
	    verbose_name = 'Фирма'
	    verbose_name_plural = 'Фирмы'