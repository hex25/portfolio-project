# Generated by Django 2.1.4 on 2019-01-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190104_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publ_date',
            field=models.DateTimeField(),
        ),
    ]