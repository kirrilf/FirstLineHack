# Generated by Django 2.2.6 on 2019-10-26 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wheel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subparagraphs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subparagraphs', models.CharField(blank=True, max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subparagraphs', to='wheel.Wheel')),
            ],
        ),
    ]
