from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account, DebitCard, CreditCard
# from balances.views import DebitCardViewSet



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class DebitCardSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = DebitCard
        fields = ['id', 'card_number', 'expiration_date', 'cvv']  


class CreditCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['id', 'card_number', 'expiration_date', 'cvv', 'credit_limit', 'interest_rate']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True)
    # debit_card = serializers.PrimaryKeyRelatedField(queryset=DebitCard.objects.all(), allow_null=True)
    # credit_card = serializers.PrimaryKeyRelatedField(queryset=CreditCard.objects.all(), allow_null=True)

    debit_card = serializers.HyperlinkedIdentityField(view_name='debitcard-detail')
    credit_card = serializers.HyperlinkedIdentityField(view_name='creditcard-detail')


    class Meta:
        model = Account
        fields = ['owner', 'opening_date', 'balance', 'debit_card', 'credit_card', 'interest_rate', 'currency', 'status']
