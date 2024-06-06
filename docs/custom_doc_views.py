from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.permissions import AllowAny


class CustomSpectacularAPIView(SpectacularAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]

class CustomSpectacularSwaggerView(SpectacularSwaggerView):
    authentication_classes = []
    permission_classes = [AllowAny]