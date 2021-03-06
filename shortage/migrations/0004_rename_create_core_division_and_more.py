# Generated by Django 4.0.2 on 2022-03-14 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0003_rename_id_core_corehistory_core_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='core',
            old_name='create',
            new_name='division',
        ),
        migrations.RenameField(
            model_name='core',
            old_name='procurement_comments',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='core',
            name='plant',
        ),
        migrations.RemoveField(
            model_name='core',
            name='production_comments',
        ),
        migrations.AddField(
            model_name='core',
            name='material',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
