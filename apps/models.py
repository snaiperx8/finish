from django.db import models
from django.contrib.auth.models import User

class CreatePost(models.Model):
	title = models.CharField(max_length = 100, verbose_name = 'Заголовок')
	image = models.ImageField(upload_to = 'posts', verbose_name = ' ', blank=True)
	text = models.TextField(verbose_name = ' ')
	date = models.DateField(auto_now_add=True, verbose_name = 'Заголовок')
	autor = models.CharField(max_length = 100, verbose_name = 'Заголовок')
# Create your models here.
