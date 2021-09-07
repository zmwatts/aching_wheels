# Generated by Django 3.2.5 on 2021-09-07 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('missing_persons', '0002_auto_20210907_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eyecolor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('GRN', 'GREEN'), ('BLU', 'BLUE'), ('BLK', 'BLACK'), ('BRN', 'BROWN'), ('HZL', 'HAZEL'), ('OTR', 'OTHER')], max_length=13)),
            ],
        ),
        migrations.AlterField(
            model_name='missing_person',
            name='eyecolor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='missing_persons.eyecolor'),
        ),
    ]
