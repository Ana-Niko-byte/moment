# Generated by Django 4.2.13 on 2024-07-05 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('charity', '0010_charity_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canvas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canvas_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charity_canvas', to='charity.charity')),
                ('contributors', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
