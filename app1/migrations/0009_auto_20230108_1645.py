# Generated by Django 3.2.16 on 2023-01-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_robot_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='RobotData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robot_data', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='robot',
            name='timestamp_all',
            field=models.ManyToManyField(to='app1.RobotData'),
        ),
    ]
