from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings    
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                             context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api/', include('api.urls')),
    path("frontend/", include("frontend.urls")),
    path('user/', include('users.urls')),
    path("students/", include("students.urls")),
    path("parcean/", include("parcean.urls")),
    path('academics/', include('questions.urls')),
    path('shops/', include('shops.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

