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
