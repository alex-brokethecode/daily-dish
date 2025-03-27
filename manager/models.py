from django.db import models


class BusinessInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Business Name')
    logo = models.ImageField(upload_to='business/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    business_hour = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    facebook_url = models.URLField(blank=True, verbose_name='Facebook URL')
    instagram_url = models.URLField(blank=True, verbose_name='Instagram URL')
    tiktok_url = models.URLField(blank=True, verbose_name='TikTok URL')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Business Information'
        verbose_name_plural = 'Business Information'

    def __str__(self):
        return f'Business: {self.name}'
