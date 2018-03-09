# Generated by Django 2.0.3 on 2018-03-09 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField(verbose_name='date published')),
                ('content', models.CharField(max_length=2000)),
            ],
        ),
    ]
