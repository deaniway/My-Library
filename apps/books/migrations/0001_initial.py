# Generated by Django 5.0.6 on 2024-07-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('is_borrowed', models.BooleanField(default=False)),
                ('borrowed_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
