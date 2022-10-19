# Generated by Django 4.1.2 on 2022-10-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate', '0006_companies_href_companies_logo_companies_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='company',
        ),
        migrations.RemoveField(
            model_name='companies',
            name='advocates',
        ),
        migrations.AddField(
            model_name='companies',
            name='advocates',
            field=models.ManyToManyField(blank=True, null=True, to='advocate.advocate'),
        ),
    ]
