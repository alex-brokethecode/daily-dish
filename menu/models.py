from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


# NOTE: Allow user to fix input errors in sold items
# NOTE: Add a button to add dishes for the daily menu (In case user want to add a new one)
# NOTE: Add categories for soups and main dishes
# NOTE: Add information of attention (free drink or yapa)


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')
    image = models.ImageField(upload_to='dishes/', verbose_name='Imagen')
    price = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='Precio')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    class Meta:
        verbose_name = 'Platillo'
        verbose_name_plural = 'Platillos'
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    date = models.DateField(unique=True, verbose_name='Fecha')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
        ordering = ('-date', )

    def __str__(self) -> str:
        return f'Menu for {self.date}'

    def total_revenue(self):

        return sum(
            item.total_sales() for item in self.menu_items.all()  # type: ignore
        )


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='menu_items')
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE, related_name='menu_items', verbose_name='Platillo')
    stock = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)])
    sold = models.PositiveSmallIntegerField(default=0, verbose_name='Vendidos')
    price_at_sale = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, verbose_name='Precio de Venta')

    class Meta:
        verbose_name = 'Platillo en Menu'
        verbose_name_plural = 'Platillos en Menu'
        # A dish can appear only once per menu
        unique_together = ('menu', 'dish',)

    def __str__(self) -> str:
        return f'{self.dish.name} in {self.menu}'

    def remaining_stock(self):
        return self.stock - self.sold

    def total_sales(self):
        return self.sold * self.price_at_sale

    def clean(self):
        # Validation for sold dishes and stock
        if self.sold > self.stock:
            raise ValidationError('Número de platos vendidos mayor al stock')

    def save(self, *args, **kwargs):
        # Validate before saving
        self.clean()

        # If it's a new entry and price_at_sale is not set, use the current dish price
        if not self.price_at_sale:
            self.price_at_sale = self.dish.price
        super().save(*args, **kwargs)
