# Generated by Django 3.1.4 on 2021-01-03 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backlogs_App', '0003_delete_backlogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backlogs',
            fields=[
                ('active_backlogs', models.IntegerField()),
                ('B_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Backlogs_App.student')),
            ],
        ),
    ]
