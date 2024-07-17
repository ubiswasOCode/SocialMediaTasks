from django.shortcuts import render
from django.http import HttpResponse
import re
from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status, generics, filters, views,mixins
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny


# Create your views here.
def Index(request):

    return render (request,'loginUsers.html')

def GetId(request):
    data = {
    "orders": [
        {"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5},
        {"id": 6}, {"id": 7}, {"id": 8}, {"id": 9}, {"id": 10},
        {"id": 11}, {"id": 648}, {"id": 649}, {"id": 650},
        {"id": 651}, {"id": 652}, {"id": 653}
    ],
    "errors": [
        {"code": 3, "message": "[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}
    ]
    }   
    data_str = str(data)
    getData = re.findall(r'\b\d+\b', data_str)

    numeric_values = list(map(int, getData))
    print(numeric_values)

    return HttpResponse('Show the data')



def AddApps(request):
     
    return render(request,'socialmedia.html')


def FacebookTemp(request):
   
    return render(request,'facebookMedia.html')


def AllSocialMedia(request):

    AppsData=APP.objects.all()
    response_data = {
        'AppsData': AppsData
    }
    return render(request,"AllSocialMedia.html",response_data)



def SocialMediaDetails(request, app_id):
    app = get_object_or_404(APP, id=app_id)
    return render(request, "SocialMediaDetailsPage.html", {'app': app})


class Login(generics.GenericAPIView):
    def post(self,request,*args,**kwargs):
        return Response({'msg':'login succssfully','status':200})

class LoginApi(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        email = data['email']
        password = data['password']

        try:
            user = User.objects.get(email = email)
            validate = check_password(password, user.password)
            
            if validate:
                token = str(RefreshToken.for_user(user))
                access = str(RefreshToken.for_user(user).access_token)
                return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "access": access,
                "refresh": token,
                "is_staff": user.is_staff,  
                "is_superuser": user.is_superuser  
            

                })
            else:
                content = {"detail": "Password Do not Match"}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
        except:
            content = {"detail": "No active account found with the given credentials"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)



class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super(RegisterUserAPIView, self).create(request, *args, **kwargs)
        if response.status_code == 201:
            user = User.objects.get(pk = response.data['id'])

            token = str(RefreshToken.for_user(user))
            access = str(RefreshToken.for_user(user).access_token)
        
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "access": access,
            "refresh": token,
            }, 
            status = status.HTTP_201_CREATED)
        return response
    

    ###------------- Add APP name 
    
class CRUDApp(viewsets.ModelViewSet):
    queryset=APP.objects.all()
    serializer_class=AppSerializer


# ###-------All Users
class AllUsers(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=AllUserSerializer