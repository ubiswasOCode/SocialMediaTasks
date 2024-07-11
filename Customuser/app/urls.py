from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('getdata',views.GetId, name='index'),
    path('temp',views.Temp, name='temp'), 
    path('facebook',views.FacebookTemp, name='facebook'),
    path('all-social-media',views.AllSocialMedia, name='all-social-media'),  
    path('social-media-details-page',views.SocialMediaDetails, name='social-media-details-page'),
]