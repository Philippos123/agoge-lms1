# Generated by Django 4.2.16 on 2025-04-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companysettings',
            name='background_color',
        ),
        migrations.RemoveField(
            model_name='companysettings',
            name='primary_color',
        ),
        migrations.RemoveField(
            model_name='companysettings',
            name='secondary_color',
        ),
        migrations.RemoveField(
            model_name='companysettings',
            name='text_color',
        ),
        migrations.AddField(
            model_name='companysettings',
            name='dashboard_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coursetobuy',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian'), ('SE', 'Swedish'), ('DE', 'German'), ('FR', 'French'), ('IT', 'Italian'), ('ES', 'Spanish'), ('FA', 'Persian')], default='EN', max_length=2),
        ),
        migrations.AlterField(
            model_name='scormpackage',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian'), ('SE', 'Swedish'), ('DE', 'German'), ('FR', 'French'), ('IT', 'Italian'), ('ES', 'Spanish'), ('FA', 'Persian')], default='EN', help_text='Språkkod för detta SCORM-paket', max_length=2),
        ),
    ]
