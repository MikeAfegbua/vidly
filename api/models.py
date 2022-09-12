from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        allowed_methods = ['get']
        resource_name = 'movies'  # for the endpoint name /movies
        excudes = ['date_created']
