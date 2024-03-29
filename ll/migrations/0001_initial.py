# Generated by Django 3.0.4 on 2020-06-30 04:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=10)),
                ('project_name', models.CharField(max_length=50)),
                ('client', models.CharField(max_length=30)),
                ('project_location', models.CharField(max_length=100)),
                ('market_sector', models.CharField(max_length=40)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projectnumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Projectname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.Projectnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Projectlocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.Projectnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.Projectnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Marketsector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.Projectnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('division', models.CharField(max_length=20)),
                ('discipline', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('linkfile', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='projectnumber', chained_model_field='projectnumber', on_delete=django.db.models.deletion.CASCADE, to='ll.Client')),
                ('marketsector', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='projectnumber', chained_model_field='projectnumber', on_delete=django.db.models.deletion.CASCADE, to='ll.Marketsector')),
                ('memo', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='projectnumber', chained_model_field='projectnumber', null=True, on_delete=django.db.models.deletion.CASCADE, to='ll.Memo')),
                ('projectlocation', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='projectnumber', chained_model_field='projectnumber', on_delete=django.db.models.deletion.CASCADE, to='ll.Projectlocation')),
                ('projectname', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='projectnumber', chained_model_field='projectnumber', on_delete=django.db.models.deletion.CASCADE, to='ll.Projectname')),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.Projectnumber')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='projectnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.Projectnumber'),
        ),
    ]
