# Generated by Django 5.0.6 on 2024-06-25 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_phone_no'),
        ('post', '0002_alter_post_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]