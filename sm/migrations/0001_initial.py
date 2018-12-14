# Generated by Django 2.1.3 on 2018-12-13 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pm', '0006_auto_20181213_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sprint', models.IntegerField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('activity', models.CharField(max_length=50)),
                ('story', models.CharField(max_length=10)),
                ('points', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.Teams')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.Tracks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.Users')),
            ],
        ),
        migrations.CreateModel(
            name='UpsDowns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sprint', models.IntegerField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('up', models.CharField(max_length=300)),
                ('down', models.CharField(max_length=300)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.Teams')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.Tracks')),
            ],
        ),
    ]
