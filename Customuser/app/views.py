from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.
def Index(request):

    return HttpResponse('Hello World')

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



def Temp(request):
     
    return render(request,'socialmedia.html')


def FacebookTemp(request):
   
    return render(request,'facebookMedia.html')


def AllSocialMedia(request):

    return render(request,"AllSocialMedia.html")


def SocialMediaDetails(request):

    return render(request,"SocialMediaDetailsPage.html")




