from django.db import models


class Brand(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand


class Color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color


class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    main_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    value = models.IntegerField()
    production_costs = models.IntegerField()
    transportation_costs = models.IntegerField()

    @property
    def total(self):
        return self.production_costs + self.transportation_costs
