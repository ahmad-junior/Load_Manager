# Generated by Django 4.1.5 on 2023-02-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Load_Menu', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CardItem',
        ),
        migrations.AlterField(
            model_name='loadmenu',
            name='date',
            field=models.DateField(),
        ),
    ]
