# Generated by Django 4.0.6 on 2022-08-26 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DSMS', '0003_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=20)),
                ('product_quantity', models.IntegerField(default=0)),
                ('brand', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='approvals',
            new_name='Approval',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
