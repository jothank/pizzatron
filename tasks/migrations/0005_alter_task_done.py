# Generated by Django 4.0.4 on 2022-06-23 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('doing', 'doing'), ('done', 'done')], max_length=5),
        ),
    ]
