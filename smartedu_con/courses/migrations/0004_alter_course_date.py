# Generated by Django 4.0.6 on 2022-07-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
