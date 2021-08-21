from django.contrib import admin
from django.conf.urls import url, re_path
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from credit_card.views import CreditCardRecordViewset, CreditCardBillsUploadView

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'credit-card-records', CreditCardRecordViewset, basename="credit-card-records")
#router.register(r'bill-upload', CreditCardBillsUploadView, basename='credit-card-bills-upload')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    url(r"__admin__/", admin.site.urls),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('api-token-auth', views.obtain_auth_token),
    url('bill-upload', CreditCardBillsUploadView.as_view())
]