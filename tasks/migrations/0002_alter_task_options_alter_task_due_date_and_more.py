# Generated by Django 5.0.7 on 2024-08-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(4, 'Low'), (3, 'Medium'), (2, 'High'), (1, 'Urgent')], default=4),
        ),
    ]
