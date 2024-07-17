from django.urls import path
from . import views
from rest_framework import routers




router=routers.DefaultRouter()


router.register('app',views.CRUDApp,basename='app')
router.register('alluser',views.AllUsers,basename='alluser')



urlpatterns = [
    path('', views.Index, name='index'),
    path('getdata',views.GetId, name='index'),
    path('add-app',views.AddApps, name='add-app'), 
    path('facebook',views.FacebookTemp, name='facebook'),
    path('all-social-media',views.AllSocialMedia, name='all-social-media'),  
    path('social-media-details-page/<int:app_id>/',views.SocialMediaDetails, name='social-media-details-page'),


    path('login/', views.LoginApi.as_view(), name='LoginApi'),
    path('register/',views.RegisterUserAPIView.as_view()),
]

urlpatterns += router.urls