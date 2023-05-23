from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Account(models.Model):
    owner = models.OneToOneField('auth.User', related_name='accounts', on_delete=models.CASCADE)
    opening_date = models.DateTimeField(default=timezone.now)
    balance = models.DecimalField(max_digits=10, decimal_places=2)   
    debit_card = models.OneToOneField('DebitCard', on_delete=models.SET_NULL, null=True, blank=True)
    credit_card = models.OneToOneField('CreditCard', on_delete=models.SET_NULL, null=True, blank=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        # Add other currencies as needed
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Suspended', 'Suspended'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open') 

    class Meta:
        ordering = ['opening_date']



class DebitCard(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    expiration_date = models.DateField()
    cvv = models.IntegerField()
    
    # ... other fields as needed ...
    
    def __str__(self):
        return self.card_number
    
class CreditCard(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    expiration_date = models.DateField()
    cvv = models.IntegerField()
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    # ... other fields as needed ...
    
    def __str__(self):
        return self.card_number