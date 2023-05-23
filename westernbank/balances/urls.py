from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from balances import views
from balances.views import AccountViewSet, UserViewSet, api_root


# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'accounts', views.AccountViewSet, basename="account")
# router.register(r'users', views.UserViewSet, basename="user")

# urlpatterns = format_suffix_patterns([
#     path('', include(router.urls)),
#     path('', api_root),
# ])

# API endpoints
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'debit-cards', views.DebitCardViewSet)
router.register(r'credit-cards', views.CreditCardViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # For login and logout views
    path('api/', views.api_root),
]

