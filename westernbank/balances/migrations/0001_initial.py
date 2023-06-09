# Generated by Django 4.2.1 on 2023-05-22 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16, unique=True)),
                ('expiration_date', models.DateField()),
                ('cvv', models.IntegerField()),
                ('credit_limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='DebitCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16, unique=True)),
                ('expiration_date', models.DateField()),
                ('cvv', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR')], default='USD', max_length=3)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Suspended', 'Suspended')], default='Open', max_length=10)),
                ('credit_card', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='balances.creditcard')),
                ('debit_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='balances.debitcard')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['opening_date'],
            },
        ),
    ]
