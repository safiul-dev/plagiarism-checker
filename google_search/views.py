from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .textGoogleMatch import GooglePlagiarismCheck

@csrf_exempt
@api_view(["POST"])
def googleSearch(request):
    
    if (request.method == 'POST'):

        copied_content="মিষ্টির দোকান থেকে দই কিনে রাস্তা দিয়ে হাঁটছি এমন সময় এক গাড়ী পুলিশ এসে দাঁড়ালো আমার সামনে।"

        google_obj = GooglePlagiarismCheck()
        data = google_obj.searchGoogle(copied_content)
        return Response(data)