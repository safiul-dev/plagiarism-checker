from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .text_extract import ImageConverter

@csrf_exempt
@api_view(["POST"])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def extractTextFromImage(request):
    
    if (request.method == 'POST'):
        
        image_obj = ImageConverter()
        image = request.FILES["image"]
        text = image_obj.convert(image)
        return Response(text)
