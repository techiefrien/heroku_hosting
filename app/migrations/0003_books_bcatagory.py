# Generated by Django 4.2.5 on 2023-12-05 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_books_download_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='bcatagory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.catagory'),
            preserve_default=False,
        ),
    ]