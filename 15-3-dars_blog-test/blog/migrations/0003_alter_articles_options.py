# Generated by Django 4.1.7 on 2023-03-28 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_articles_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ('-title',), 'verbose_name': 'Maqola', 'verbose_name_plural': 'Maqolalar'},
        ),
    ]
