# Generated by Django 3.0.3 on 2020-10-24 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_auto_20201024_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPlaceKeeper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Keeper_travel_name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Traveluser',
        ),
        migrations.RenameField(
            model_name='travel',
            old_name='type_travel',
            new_name='travel_detail',
        ),
        migrations.RenameField(
            model_name='traveltype',
            old_name='travel_detail',
            new_name='type_travel',
        ),
        migrations.RemoveField(
            model_name='traveltype',
            name='travel_name',
        ),
        migrations.RemoveField(
            model_name='traveltype',
            name='travel_wherename',
        ),
        migrations.AddField(
            model_name='travel',
            name='travel_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='travel',
            name='travel_wherename',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='travelplacekeeper',
            name='travel_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.Travel'),
        ),
    ]
