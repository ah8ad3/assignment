# Generated by Django 5.0.2 on 2024-02-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Content')),
                ('rating_count', models.PositiveIntegerField(default=0, verbose_name='Rating Count')),
                ('rating_average', models.FloatField(default=0, verbose_name='Rating Average')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
            },
        ),
    ]
