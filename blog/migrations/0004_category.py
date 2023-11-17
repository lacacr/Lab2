# Generated by Django 4.2.7 on 2023-11-15 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descrição', models.TextField()),
                ('post', models.ManyToManyField(to='blog.post')),
            ],
        ),
    ]