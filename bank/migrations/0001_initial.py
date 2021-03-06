# Generated by Django 3.0.2 on 2020-04-25 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('email', models.EmailField(max_length=128)),
                ('dob', models.DateField(max_length=8)),
                ('phone', models.CharField(max_length=10)),
                ('blood_group', models.CharField(choices=[(1, 'A +ve'), (2, 'B +ve'), (3, 'AB +ve'), (4, 'O +ve'), (5, 'A -ve'), (6, 'B -ve'), (7, 'AB -ve'), (8, 'O -ve')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
