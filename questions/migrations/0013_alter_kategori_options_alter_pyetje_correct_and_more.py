# Generated by Django 4.2.9 on 2024-02-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_progress_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Kategorite'},
        ),
        migrations.AlterField(
            model_name='pyetje',
            name='correct',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pyetje',
            name='option1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pyetje',
            name='option2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pyetje',
            name='option3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pyetje',
            name='option4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
