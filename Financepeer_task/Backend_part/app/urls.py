from email.policy import default
from knox import views as knox_views
from .views import LoginAPI, PostDataViewSets, RegisterAPI,FileModelViewSets
from django.urls import path
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("api",PostDataViewSets,basename="api")
router.register("upload",FileModelViewSets,basename="file")

urlpatterns = [
    path("api/register/",RegisterAPI.as_view(),name="register"),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

] 
urlpatterns +=  router.urls
