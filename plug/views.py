
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .plagiarism_check import PlagiarismChecker 
from .bangla_nltk import BanglaNltk
from .pdf_converter import PdfConverter

@csrf_exempt
@api_view(["POST"])
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


@csrf_exempt
@api_view(["POST"])
def twoPdfPlagiarismCheck(request):
    
    if (request.method == 'POST'):
        file1 = request.FILES["file1"]
        file2 = request.FILES["file2"]
        pdf_text1 = PdfConverter.converter(request.FILES["file1"])
        pdf_text2 = PdfConverter.converter(request.FILES["file2"])
        plagiarism_obj = PlagiarismChecker()
        similarText = plagiarism_obj.sentenceSimilarity(pdf_text1, pdf_text2)
        percentage = plagiarism_obj.percentageOfText(pdf_text1, pdf_text2)
        dic = {'between':file1.name + " " + file2.name,'text':similarText, 'percent': percentage}
        return JsonResponse(dic, safe=False)