# Generated by Django 4.0.5 on 2022-06-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]