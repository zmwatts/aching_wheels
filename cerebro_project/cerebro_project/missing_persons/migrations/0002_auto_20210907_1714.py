# Generated by Django 3.2.5 on 2021-09-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missing_persons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missing_person',
            name='title',
        ),
        migrations.AddField(
            model_name='missing_person',
            name='unique_markings',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
