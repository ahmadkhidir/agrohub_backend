from django.contrib import admin
from . import models

admin.site.register([
    models.Farmer,
    models.Farm,
    models.FarmLocation,
    models.FarmPhoto,
    models.FarmCrop,
])
