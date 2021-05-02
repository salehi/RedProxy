# Generated by Django 3.2 on 2021-05-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0002_keepit_query_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='keepit',
            name='response',
            field=models.TextField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='keepit',
            name='status_code',
            field=models.PositiveIntegerField(db_index=True, null=True),
        ),
    ]