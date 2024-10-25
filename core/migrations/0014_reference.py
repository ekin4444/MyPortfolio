# Generated by Django 5.0.3 on 2024-05-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_language_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('ref_name', models.CharField(blank=True, default='', help_text='This is the variable of the setting.', max_length=254, verbose_name='Reference Name')),
                ('ref_company', models.CharField(blank=True, default='', max_length=254, verbose_name='Reference Company')),
                ('ref_job', models.CharField(blank=True, default='', max_length=254, verbose_name='Reference Job')),
                ('ref_number', models.IntegerField(blank=True, default='', max_length=254, verbose_name='Reference Number')),
            ],
            options={
                'verbose_name': 'Reference',
                'verbose_name_plural': 'Reference',
                'ordering': ('ref_name',),
            },
        ),
    ]
