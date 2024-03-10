from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Last update at'), auto_now=True)

    class Meta:
        abstract = True