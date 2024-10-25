# Generated by Django 5.0.3 on 2024-05-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('language_name', models.CharField(blank=True, default='', max_length=254, verbose_name='Language')),
                ('level', models.CharField(blank=True, default='', max_length=254, verbose_name='Level')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Language',
                'ordering': ('order',),
            },
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Icon'),
        ),
    ]
