from django.db import models
 
class MovieModel(models.Model):
    movie_name=models.CharField(max_length=50)
    release_date = models.DateField()
    watch_by=models.CharField(max_length=50)


