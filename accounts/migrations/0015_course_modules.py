# Generated by Django 3.2.3 on 2021-06-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_rename_course_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleName', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50, null=True)),
                ('link', models.CharField(max_length=50, null=True)),
                ('course_id', models.IntegerField(max_length=100, null=True)),
                ('user_created', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
