from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("customers",views.CustomerViewsetView,basename="customers")


urlpatterns=[

    path("token/",ObtainAuthToken.as_view()),

    path("works/<int:pk>/",views.WorkMixinView.as_view())

]+router.urls