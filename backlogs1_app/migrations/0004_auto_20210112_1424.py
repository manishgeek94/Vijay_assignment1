# Generated by Django 3.1.4 on 2021-01-12 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backlogs1_app', '0003_auto_20210112_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backlogs',
            name='B_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backlogs1_app.student'),
        ),
    ]
