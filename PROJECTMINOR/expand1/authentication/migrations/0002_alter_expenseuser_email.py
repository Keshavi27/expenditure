# Generated by Django 4.1.7 on 2023-03-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
