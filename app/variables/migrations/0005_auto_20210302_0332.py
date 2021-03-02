# Generated by Django 3.1.7 on 2021-03-02 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('variables', '0004_variable_dependencies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variable',
            name='dependencies',
        ),
        migrations.CreateModel(
            name='FormulaVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default='01-01-1970', null=True)),
                ('child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='variables.variable')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='variables.variable')),
            ],
        ),
    ]