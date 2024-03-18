from django.db import models

class Pereval(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    beauty_title = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField()
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=20)
    user_fam = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_otc = models.CharField(max_length=255)
    coords_latitude = models.FloatField()
    coords_longitude = models.FloatField()
    coords_height = models.IntegerField()
    level_winter = models.CharField(max_length=255, blank=True)
    level_summer = models.CharField(max_length=255, blank=True)
    level_autumn = models.CharField(max_length=255, blank=True)
    level_spring = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    class Meta:
        app_label = 'restapi'

class PerevalImage(models.Model):
    pereval = models.ForeignKey(Pereval, related_name='images', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pereval_images/')

    class Meta:
        app_label = 'restapi'
