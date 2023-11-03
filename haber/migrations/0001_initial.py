# Generated by Django 4.2.4 on 2023-10-06 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Haber Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Haber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Haber Başlık')),
                ('haberText', models.TextField(verbose_name='Haber İçeriği')),
                ('haberText2', models.TextField(verbose_name='Haber İçeriği2')),
                ('haberText3', models.TextField(verbose_name='Haber İçeriği3')),
                ('haberResim', models.ImageField(upload_to=None, verbose_name='Haber Resmi')),
                ('haberResim2', models.ImageField(upload_to=None, verbose_name='Haber Resmi2')),
                ('haberResim3', models.ImageField(upload_to=None, verbose_name='Haber Resmi3')),
                ('haberZamani', models.DateField(auto_now_add=True, verbose_name='Haber Paylaşım Zamanı')),
                ('haberKategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='haber.kategori', verbose_name='Haber Kategori')),
            ],
        ),
    ]
