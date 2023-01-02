from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from .textGoogleMatch import GooglePlagiarismCheck
from nltk.tokenize import word_tokenize

@csrf_exempt
@api_view(["POST"])
@parser_classes([JSONParser])
def googleSearch(request, format=None):
    
    if (request.method == 'POST'):

        data = request.data['text']
        word_tokenize_data = word_tokenize(data)
        
        if len(word_tokenize_data) <= 80:

            google_obj = GooglePlagiarismCheck()
            data = google_obj.plag_check(data)
            return Response(data, status=200)
        
        else:
            return Response({"message": "Word is more then 300"}, status=400)


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
