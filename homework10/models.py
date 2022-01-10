from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Output(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Delivryman(models.Model):
    city = models.OneToOneField(Place, on_delete=models.CASCADE)

    def str(self):
        return f'{self.id}'


class Host(models.Model):
    city = models.ForeignKey(Place, on_delete=models.CASCADE)
    product = models.ManyToManyField(Output)

    def str(self):
        return f'{self.id}'

