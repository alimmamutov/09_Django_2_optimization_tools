# Generated by Django 3.2.8 on 2022-01-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='langs',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='язык'),
        ),
    ]