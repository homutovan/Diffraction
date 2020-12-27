# Generated by Django 3.1.3 on 2020-12-11 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='JsonTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('column1', models.CharField(max_length=30)),
                ('column2', models.CharField(max_length=30)),
                ('column3', models.CharField(blank=True, max_length=30, null=True)),
                ('column4', models.CharField(blank=True, max_length=30, null=True)),
                ('column5', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Информация о товаре')),
                ('image', models.ManyToManyField(related_name='product', to='products_services.Image')),
                ('table', models.ManyToManyField(related_name='product', to='products_services.Table')),
            ],
        ),
        migrations.CreateModel(
            name='LineTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column1', models.CharField(max_length=70)),
                ('column2', models.CharField(max_length=70)),
                ('column3', models.CharField(blank=True, max_length=70, null=True)),
                ('column4', models.CharField(blank=True, max_length=70, null=True)),
                ('column5', models.CharField(blank=True, max_length=70, null=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='products_services.table')),
            ],
        ),
    ]