from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views 
from rest_framework.routers import DefaultRouter
from practice_app4 import views

#create router object
router=DefaultRouter()

#register StudentViewSets with Router
router.register('studentapi',views.StudentViewSets,basename="studentapi")


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('practice_app1.urls')),
    # path('',include('practice_app2.urls')),
    # path('',include('practice_app3.urls')),
    path('',include(router.urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    
]
