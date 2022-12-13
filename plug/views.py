
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .plagiarism_check import PlagiarismChecker 
from .bangla_nltk import BanglaNltk

@csrf_exempt
@api_view(['GET', "POST"])
def twoTextPlagiarismCheck(request):
    
    if (request.method == 'POST'):
        plagiarism_obj = PlagiarismChecker()
        b_nltk = BanglaNltk()
        doc1 = request.POST['doc1']
        doc2 = request.POST['doc2']
        text1 = b_nltk.sentence_tokenizer(doc1)
        text2 = b_nltk.sentence_tokenizer(doc2)

        arrayOfResult = plagiarism_obj.plugCheckFromTextArray(text1, text2)
        dic = {'text':arrayOfResult[0], 'percent': arrayOfResult[1]}
        
        return Response(dic)