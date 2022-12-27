from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .textGoogleMatch import GooglePlagiarismCheck

@csrf_exempt
@api_view(["POST"])
def googleSearch(request):
    
    if (request.method == 'POST'):

        text = request.POST.get('text') 
        google_obj = GooglePlagiarismCheck()
        # data = google_obj.plag_check(text)
        return Response(text, status=200)


@csrf_exempt
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getSomeData (request):

    data = [{
        "hello": 1
    },{
        "hello": 3
    }
    ]
    return Response(data)
