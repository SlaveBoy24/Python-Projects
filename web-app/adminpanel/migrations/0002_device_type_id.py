# Generated by Django 4.2.11 on 2024-04-23 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='type_id',
            field=models.ForeignKey(default=int, on_delete=django.db.models.deletion.DO_NOTHING, to='adminpanel.type'),
            preserve_default=False,
        ),
    ]
