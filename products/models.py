from django.db import models
from django_seed import Seed


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass


seeder = Seed.seeder()

seeder.add_entity(User, 5)

inserted_pks = seeder.execute()
