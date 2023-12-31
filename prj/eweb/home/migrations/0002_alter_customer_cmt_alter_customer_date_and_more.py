# Generated by Django 4.2.6 on 2023-10-11 11:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="cmt",
            field=models.CharField(max_length=1000, verbose_name="comments"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=100, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.BigIntegerField(verbose_name="phone"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="service",
            field=models.CharField(
                choices=[
                    ("Aadhar Card", "Aadhar Card"),
                    ("Pan Card", "Pan Card"),
                    ("Voter ID Card", "Voter ID Card"),
                    ("Government Services", "Government Services"),
                    ("Add Money to Wallet", "Add Money to Wallet"),
                    ("Withdrawn Money from Wallet", "Withdraw Money from Wallet"),
                    ("Utility Bills", "Utility Bills"),
                ],
                max_length=100,
                verbose_name="service",
            ),
        ),
    ]
