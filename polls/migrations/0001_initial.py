# Generated by Django 4.0.3 on 2023-06-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pr_img1', models.ImageField(default='', upload_to='polls/images')),
                ('pr_img2', models.ImageField(default='', upload_to='polls/images')),
                ('pr_img3', models.ImageField(default='', upload_to='polls/images')),
                ('pr_img4', models.ImageField(default='', upload_to='polls/images')),
                ('pr_img5', models.ImageField(default='', upload_to='polls/images')),
                ('pr_rv1', models.ImageField(default='', upload_to='polls/images')),
                ('pr_rv2', models.ImageField(default='', upload_to='polls/images')),
                ('pr_rv3', models.ImageField(default='', upload_to='polls/images')),
                ('pr_rv4', models.ImageField(default='', upload_to='polls/images')),
                ('product_name', models.CharField(max_length=500)),
                ('old_price', models.IntegerField(default=0)),
                ('new_price', models.IntegerField(default=0)),
                ('off', models.CharField(default=0, max_length=80)),
                ('desc', models.CharField(max_length=900)),
            ],
        ),
    ]
