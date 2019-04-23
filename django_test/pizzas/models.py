from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    attr = 'haha'

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=None)
    name = models.TextField()
    attr = 'hehe'

    def __str__(self):
        return self.name[:30]

