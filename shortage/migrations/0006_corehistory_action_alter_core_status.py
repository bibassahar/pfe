# Generated by Django 4.0.2 on 2022-03-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0005_alter_core_closing_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='corehistory',
            name='action',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='core',
            name='status',
            field=models.CharField(default='To do', max_length=30, null=True),
        ),
    ]
