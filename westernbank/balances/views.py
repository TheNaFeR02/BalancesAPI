from rest_framework import viewsets
from django.contrib.auth.models import User
from balances.serializers import UserSerializer
from rest_framework import permissions
from balances.models import Account
from balances.serializers import AccountSerializer 
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from balances.models import DebitCard
from balances.serializers import DebitCardSerializer
from balances.models import CreditCard
from balances.serializers import CreditCardSerializer
from balances.permissions import IsOwner

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        elif user.is_authenticated:
            return User.objects.filter(id=user.id)
        return User.objects.none()
        

    
class AccountViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Account.objects.all()
        elif user.is_authenticated:
            return Account.objects.filter(owner=user.id)
        return Account.objects.none()

class DebitCardViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = DebitCard.objects.all()
    serializer_class = DebitCardSerializer
    # permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        
        if user.is_superuser:
            return DebitCard.objects.all()
        elif user.is_authenticated:
            card_number = Account.objects.get(owner = user).debit_card
            return DebitCard.objects.filter(card_number = card_number)
            
        return DebitCard.objects.none()

class CreditCardViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    # permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        
        if user.is_superuser:
            return CreditCard.objects.all()
        elif user.is_authenticated:
            card_number = Account.objects.get(owner = user).credit_card
            return CreditCard.objects.filter(card_number=card_number)
        return CreditCard.objects.none()


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'accounts': reverse('account-list', request=request, format=format)
    })