# Generated by Django 4.1.2 on 2022-10-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate', '0002_remove_company_advocate_remove_links_advocate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='advocates',
            field=models.ManyToManyField(blank=True, null=True, related_name='companies', to='advocate.advocate'),
        ),
    ]
