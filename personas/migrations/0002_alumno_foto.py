# Generated by Django 3.1.1 on 2020-10-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]
