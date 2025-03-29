from django.db import models


class BusinessInfo(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Nombre')
    logo = models.ImageField(upload_to='business/',
                             blank=True, null=True,
                             verbose_name='Logo')
    address = models.CharField(max_length=255,
                               blank=True,
                               verbose_name='Dirección')
    business_hour = models.CharField(max_length=255,
                                     blank=True,
                                     verbose_name='Horario de atención')
    phone_number = models.CharField(max_length=20,
                                    blank=True,
                                    verbose_name='Número de contacto')
    facebook_url = models.URLField(blank=True,
                                   verbose_name='Facebook')
    instagram_url = models.URLField(blank=True,
                                    verbose_name='Instagram')
    tiktok_url = models.URLField(blank=True, verbose_name='TikTok')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    class Meta:
        verbose_name = 'Información del Negocio'
        verbose_name_plural = 'Información del Negocio'

    def __str__(self):
        return f'Business: {self.name}'
