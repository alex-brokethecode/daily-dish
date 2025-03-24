from django.db import models
from django.core.validators import MaxValueValidator


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='dishes/')
    quantity = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)])
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name
