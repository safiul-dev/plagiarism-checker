
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', "POST"])
def checkPlagiarism(request):
    
    if (request.method == 'POST'):
        doc1 = request.POST['doc1']
        doc2 = request.POST['doc2']

        return Response()