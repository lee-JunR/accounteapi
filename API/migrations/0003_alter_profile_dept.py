# Generated by Django 3.2.5 on 2021-07-08 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_profile_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dept',
            field=models.CharField(choices=[('mju', 'MJU'), ('not-specified', 'Not Specified'), ('uplex', 'UPLEX')], max_length=100, null=True),
        ),
    ]
