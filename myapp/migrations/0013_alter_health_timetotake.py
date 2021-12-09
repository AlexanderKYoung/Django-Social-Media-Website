# Generated by Django 3.2.7 on 2021-10-31 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_activities_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='timeToTake',
            field=models.CharField(choices=[('Once daily', 'Once daily'), ('Two times a day', 'Two times a day'), ('Once nightly', 'Once nightly'), ('Once a week', 'Once a week'), ('Once every other day', 'Once every other day')], default='Once daily', max_length=20),
        ),
    ]
