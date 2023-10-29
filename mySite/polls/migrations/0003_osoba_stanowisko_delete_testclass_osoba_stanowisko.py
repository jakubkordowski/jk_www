# Generated by Django 4.2.6 on 2023-10-23 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_testclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=20)),
                ('nazwisko', models.CharField(max_length=30)),
                ('plec', models.IntegerField(choices=[(1, 'Kobieta'), (2, 'Mezczyzna'), (3, 'Inne')], default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
                ('opis', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='testClass',
        ),
        migrations.AddField(
            model_name='osoba',
            name='stanowisko',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.stanowisko'),
        ),
    ]
