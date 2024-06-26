from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.


class Categ(models.Model):
    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(max_length=100, unique = True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'catagory'
        verbose_name_plural = 'catagories' 


    def __str__(self):
        return'{}'.format(self.name)
    
    def get_url(self):
        return reverse('prod_cat',args=[self.slug])


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    img = models.ImageField(upload_to='Products')
    desc = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(Categ,on_delete= models.CASCADE)

    def __str__(self):
        return'{}'.format(self.name)
    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])