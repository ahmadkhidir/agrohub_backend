# Generated by Django 5.0.3 on 2024-03-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_farmphoto_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmphoto',
            name='caption',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
