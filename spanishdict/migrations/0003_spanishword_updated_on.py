# Generated by Django 4.1.2 on 2023-01-04 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spanishdict', '0002_alter_spanishword_primary_eng_translation'),
    ]

    operations = [
        migrations.AddField(
            model_name='spanishword',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]