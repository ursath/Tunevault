# Generated by Django 4.2.5 on 2023-09-07 20:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('post_id', models.CharField(max_length=50)),
                ('comment_answer_id', models.CharField(default=0, max_length=50)),
                ('likes', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('content', models.TextField(max_length=597)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('vault_id', models.CharField(max_length=50)),
                ('likes', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('title', models.TextField(max_length=60)),
                ('content', models.TextField(max_length=597)),
            ],
        ),
        migrations.CreateModel(
            name='Vault',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('bio', models.TextField(blank=True)),
                ('profileimg', models.ImageField(default='profile_image.jpg', upload_to='profile_image')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
