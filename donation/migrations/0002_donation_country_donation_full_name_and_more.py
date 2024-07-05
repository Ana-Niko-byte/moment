# Generated by Django 4.2.13 on 2024-07-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='country',
            field=models.CharField(default='Ireland', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='full_name',
            field=models.CharField(default='Jane Smith', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
