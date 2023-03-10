# Generated by Django 4.1.7 on 2023-03-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_expenseuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='PocketMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('month', models.CharField(max_length=30)),
            ],
        ),
    ]