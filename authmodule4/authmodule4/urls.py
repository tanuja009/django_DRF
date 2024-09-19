from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from authapp4 import views
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('studentapi',views.MyModelViewSet,basename="studentapi")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('getapi/',obtain_auth_token)

    
]

urlpatterns += router.urls
