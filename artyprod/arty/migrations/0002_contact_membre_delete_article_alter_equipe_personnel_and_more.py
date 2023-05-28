# Generated by Django 4.2 on 2023-05-14 17:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cv', models.FileField(upload_to='cvs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])),
                ('image', models.ImageField(upload_to='images/')),
                ('linkedin', models.URLField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AlterField(
            model_name='equipe',
            name='personnel',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Personnel',
        ),
        migrations.AddField(
            model_name='membre',
            name='groupe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arty.equipe'),
        ),
    ]
