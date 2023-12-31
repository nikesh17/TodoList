# Generated by Django 4.1.4 on 2023-01-29 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='todolist')),
                ('task_date', models.DateField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('lowest', 'Lowest'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('highest', 'Highest')], default='lowest', max_length=100)),
                ('is_done', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todofeature.category')),
                ('labels', models.ManyToManyField(blank=True, to='todofeature.label')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
