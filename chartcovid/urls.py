from django.urls import path, include
from .views import country_list, country_detail, CountryAPIView, CountryDetails, GenericAPIView, CountryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('country', CountryViewSet, basename = 'country')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),


    path('country/', CountryAPIView.as_view()),
    path('detail/<int:id>/', CountryDetails.as_view()),
    path('country/<int:id>/', GenericAPIView.as_view()),
]
