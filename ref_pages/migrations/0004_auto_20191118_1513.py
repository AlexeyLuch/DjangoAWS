# Generated by Django 2.2.7 on 2019-11-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref_pages', '0003_referer_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referer',
            name='img',
            field=models.ImageField(default='my_site/media/img/q12.jpg', upload_to='my_site/ref_pages/templates/ref_pages/img'),
        ),
    ]