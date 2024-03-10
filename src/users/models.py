from django.contrib.auth.models import AbstractUser, UserManager
from utilities.models import BaseModel, models
from utilities import helpers


SOCIAL_MEDIA_CHOICES = (
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
    ('instagram', 'Instagram'),
    ('linkedin', 'LinkedIn'),
    ('whatsapp', 'WhatsApp'),
    ('telegram', 'Telegram'),
    ('youtube', 'YouTube'),
    ('pinterest', 'Pinterest'),
    ('snapchat', 'Snapchat'),
    ('tiktok', 'TikTok'),
    ('other', 'Other'),
)


class User(AbstractUser, BaseModel):
    created_at = None

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class SocialMedia(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(choices=SOCIAL_MEDIA_CHOICES, max_length=20)
    username = models.CharField(max_length=100)


class Farmer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()


class Farm(BaseModel):
    owner = models.ForeignKey('Farmer', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    crops = models.ManyToManyField('Crop', blank=True, null=True)


class FarmLocation(BaseModel):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=12)
    farm = models.OneToOneField(Farm, on_delete=models.CASCADE)


class FarmPhoto(BaseModel):
    photo = models.ImageField(upload_to=helpers.farm_photos_path)
    caption = models.CharField(max_length=300, blank=True, null=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Delete the old image
        old_instance = FarmPhoto.objects.filter(pk=self.pk).first()
        if old_instance:
            old_instance.photo.delete(save=False)
        super().save(*args, **kwargs)


class Crop(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to=helpers.farm_crop_photos_path)
    family = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    planting_season = models.CharField(max_length=100)
    harvest_season = models.CharField(max_length=100)