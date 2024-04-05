# Generated by Django 5.0.2 on 2024-03-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0002_rename_generalsettings_generalsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of the settings', max_length=255, verbose_name='name')),
                ('description', models.CharField(blank=True, default='', max_length=255, verbose_name='description')),
                ('file', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Image')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
            ],
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='name',
            field=models.CharField(blank=True, default='', help_text='This is variable of the settings', max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='parameter',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='parameter'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_date'),
        ),
    ]
