from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(["POST"])
def extractTextFromImage(request):
    
    if (request.method == 'POST'):

        dic = {"hello": "world"}
        return Response(dic)
