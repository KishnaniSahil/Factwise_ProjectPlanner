# Generated by Django 4.2.7 on 2023-11-09 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageusersapp', '0003_team_members_task_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user_assigned',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
