from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class CreatePost(models.Model):
	title = models.CharField(max_length = 100, verbose_name = 'Заголовок')
	image = models.ImageField(upload_to = 'posts', verbose_name = False, blank=True)
	text = RichTextField(verbose_name = False)
	date = models.DateField(auto_now_add=True)
	autor = models.CharField(max_length = 100)
	
# Create your models here.
