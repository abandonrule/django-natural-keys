# Generated by Django 2.2.3 on 2019-07-26 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithSingleUniqueField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NaturalKeyParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('group', models.CharField(max_length=10)),
            ],
            options={
                'unique_together': {('code', 'group')},
            },
        ),
        migrations.CreateModel(
            name='NaturalKeyChild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=10)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.NaturalKeyParent')),
            ],
            options={
                'unique_together': {('parent', 'mode')},
            },
        ),
        migrations.CreateModel(
            name='ModelWithNaturalKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.NaturalKeyChild')),
            ],
        ),
        migrations.CreateModel(
            name='ModelWithExtraField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('date', models.DateField(max_length=10, unique=True)),
                ('extra', models.TextField()),
            ],
            options={
                'unique_together': {('code', 'date')},
            },
        ),
    ]
