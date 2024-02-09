# Generated by Django 4.2.9 on 2024-02-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_pyetje_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('correct_option', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Pyetje',
        ),
    ]