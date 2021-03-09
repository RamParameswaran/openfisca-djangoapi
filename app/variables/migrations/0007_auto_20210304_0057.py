# Generated by Django 3.1.7 on 2021-03-04 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('variables', '0006_remove_formulavariable_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulavariable',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='is_parent', to='variables.variable'),
        ),
    ]