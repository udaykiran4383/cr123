# Generated by Django 4.2.14 on 2024-07-25 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_userprofile_representative_type_userprofile_school_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeRepresentative',
            fields=[
            ],
            options={
                'verbose_name': 'College Representative',
                'verbose_name_plural': 'College Representatives',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('myapp.userprofile',),
        ),
        migrations.CreateModel(
            name='SchoolRepresentative',
            fields=[
            ],
            options={
                'verbose_name': 'School Representative',
                'verbose_name_plural': 'School Representatives',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('myapp.userprofile',),
        ),
    ]
