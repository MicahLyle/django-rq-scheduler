# Generated by Django 2.2.13 on 2020-06-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_added_args_and_kwargs_models'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobarg',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='jobkwarg',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='jobarg',
            name='arg_name',
        ),
        migrations.RemoveField(
            model_name='jobkwarg',
            name='arg_name',
        ),
        migrations.AddField(
            model_name='jobarg',
            name='arg_type',
            field=models.CharField(choices=[('str_val', 'string'), ('int_val', 'int'), ('bool_val', 'boolean'), ('datetime_val', 'Datetime')], default='str_val', max_length=12, verbose_name='Argument Type'),
        ),
        migrations.AddField(
            model_name='jobarg',
            name='bool_val',
            field=models.BooleanField(default=False, verbose_name='Boolean Value'),
        ),
        migrations.AddField(
            model_name='jobkwarg',
            name='arg_type',
            field=models.CharField(choices=[('str_val', 'string'), ('int_val', 'int'), ('bool_val', 'boolean'), ('datetime_val', 'Datetime')], default='str_val', max_length=12, verbose_name='Argument Type'),
        ),
        migrations.AddField(
            model_name='jobkwarg',
            name='bool_val',
            field=models.BooleanField(default=False, verbose_name='Boolean Value'),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='cron_string',
            field=models.CharField(help_text='Define the schedule in a crontab like syntax. Times are in UTC.', max_length=64, verbose_name='cron string'),
        ),
        migrations.AlterField(
            model_name='repeatablejob',
            name='interval_unit',
            field=models.CharField(choices=[('seconds', 'seconds'), ('minutes', 'minutes'), ('hours', 'hours'), ('days', 'days'), ('weeks', 'weeks')], default='hours', max_length=12, verbose_name='interval unit'),
        ),
    ]
