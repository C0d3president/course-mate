# Generated by Django 3.2.3 on 2021-06-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_answers_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
