# Generated by Django 4.2.5 on 2023-10-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunevault', '0002_profile_followers_vault_description_vault_followers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vault',
            name='type',
            field=models.TextField(default='null', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='media/default_profile.jpg', upload_to='media/profile_image'),
        ),
    ]
