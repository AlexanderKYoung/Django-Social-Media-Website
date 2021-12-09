# Generated by Django 3.2.7 on 2021-10-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_activities_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='type',
            field=models.CharField(choices=[('Sport', 'Sports'), ('Entertainment', 'Entertainment'), ('Movie', 'Movies'), ('Game', 'Games'), ('Fitness', 'Exercise'), ('Hangout', 'Hangout'), ('Health', 'Health')], default='Sport', max_length=20),
        ),
    ]
