# Generated by Django 4.0.6 on 2022-07-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]