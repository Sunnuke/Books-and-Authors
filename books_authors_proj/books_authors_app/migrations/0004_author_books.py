# Generated by Django 2.2.4 on 2020-11-05 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_auto_20201105_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='books_authors_app.Book'),
        ),
    ]
