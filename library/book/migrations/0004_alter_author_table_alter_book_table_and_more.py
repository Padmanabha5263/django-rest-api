# Generated by Django 4.1.1 on 2022-09-15 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_publication_website_alter_book_authorid_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='Authors',
        ),
        migrations.AlterModelTable(
            name='book',
            table='Books',
        ),
        migrations.AlterModelTable(
            name='publication',
            table='Publications',
        ),
    ]